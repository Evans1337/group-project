import json
import re
import shutil
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

related_words = ['新冠', '新型冠状', '病毒', '肺炎', '疫', '病例', '高风险', '感染',
                 '抗体', '免疫', '疫苗', '物资', '预防',
                 '医护', '医疗', '世卫', '世界卫生组织',
                 '钟南山', '陈薇', '新冠',
                 '防控', '封城', '隔离', '消毒', '消杀', '治疗', '防护', '守护',
                 '复工', '复产', '重启', '武汉', ]


def getRelatedBV():
    for i in range(1, 70):
        # 模拟浏览器
        headers = {
            'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        # 包含待爬取信息的url
        # 改
        url = 'https://api.bilibili.com/x/space/arc/search?mid=456664753&pn=%s&ps=30&jsonp=jsonp' % (i)
        # print(url)
        # 访问url
        r = requests.get(url, headers)
        # 将爬取到的json格式的数据转化为字典
        text = json.loads(r.text)
        # 取出嵌套字典里我们想要的部分
        res = text['data']['list']['vlist']
        counter = 0
        for item in res:
            counter = counter + 1
            # 以列表的形式取出对我们有用的数据
            list = ['bv: ' + item['bvid'], ' 视频标题: ' + item['title']]
            # 转化为字符串格式
            result = ''.join(list)
            # 写进文件里
            with open('CCTVnews.txt', 'a+', encoding="utf-8") as f:
                f.write(result + '\n')
        print('have read page' + str(i) + ' with ' + str(counter) + ' videos')
        time.sleep(3)


def getBiuAndSave(bv):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52'
    }
    resp = requests.get(url='https://www.bilibili.com/video/BV' + bv, headers=headers)
    match = r'cid=(.*?)&aid'
    cid = re.search(match, resp.text).group().replace('cid=', '').replace('&aid', '')

    matchVideoName = r'h1 title="(.*?)" class="video-title"'
    videoName = re.search(matchVideoName, resp.text).group().replace('h1 title="', '').replace('" class="video-title"',
                                                                                               '')

    matchTime = r'弹幕</span><span>(.*?)</span>'
    createdTime = re.search(matchTime, resp.text).group().replace('弹幕</span><span>', '').replace('</span>', '')
    createdTime = createdTime[0:10]
    # print(createdTime)

    url = 'https://comment.bilibili.com/' + cid + '.xml'  # 弹幕地址

    # 发起xml请求
    html = requests.get(url).content  # 发起请求并获得网页内容
    html_data = str(html, 'utf-8')  # 对网页进行‘utf-8’解码

    # 解析xml并提取弹幕内容
    soup = BeautifulSoup(html_data, 'lxml')
    results = soup.find_all('d')  # 找到所有的‘d'标签
    comments = [x.text for x in results]  # 提取每个’d'标签的text内容，即弹幕文字

    # 保存结果
    try:
        comments_dict = {'comments': comments[1:]}
        df = pd.DataFrame(comments_dict)
        filename = createdTime + ' ' + videoName + ' ' + bv + '.csv'
        df.to_csv(filename, encoding='utf-8')
        print('get the Biu of video:  ' + videoName)
        src = "C:/Users/17337/Desktop/bili/" + filename
        dest = "C:/Users/17337/Desktop/bili/CCTVnews"
        shutil.move(src, dest)
    except:
        print('something wrong happened in ' + videoName)

    time.sleep(3)


def get_time(created):
    return time.strftime("%Y-%m-%d", created)


if __name__ == '__main__':
    getRelatedBV()
    for line in open("CCTVnews.txt", 'r', encoding="utf-8"):
        if any(ext in line for ext in related_words):
            bv = line[6: 16]
            print(bv)
            getBiuAndSave(bv)
