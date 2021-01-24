import os

if __name__ == '__main__':
    # dirPath = './CCTVnews/bili after 3.10'
    # fileNames = os.listdir(dirPath)
    #
    # temp = ''
    #
    # for file in fileNames:
    #     with open(dirPath + '/' + file, "r", encoding='utf-8') as info:
    #         content = info.read()
    #         info.close()
    #     temp += content
    #
    # path_name = './CCTVnews/biliAfter3.10.txt'
    # with open(path_name, "a", encoding="UTF-8") as ff:
    #     ff.write(temp)
    #     ff.close()

    with open('./numbers.txt', "a+", encoding='utf-8') as f:
        for i in range(61, 3000):
            f.write(str(i) + '\n')
        f.close()
