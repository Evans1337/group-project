from snownlp import SnowNLP
import matplotlib.pyplot as plt
import numpy as np





def snowanalysis(self):
    sentimentslist = []
    for li in self:
        print(li)
        s = SnowNLP(li)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01))
    plt.show()
    print(sentimentslist)

    for i in range(len(sentimentslist)):
        if (sentimentslist[i] > 0.3):
            sentimentslist[i] = 1
        elif ((sentimentslist[i] <= 0.3) and (sentimentslist[i] >= 0.1)):
            sentimentslist[i] = 0
        elif ((sentimentslist[i] < 0.1)):
            sentimentslist[i] = -1

    print(sentimentslist)
    info = []
    a = 0
    b = 0
    c = 0
    for x in range(0, len(sentimentslist)):
        if (sentimentslist[x] == 1):
            a = a + 1
        elif (sentimentslist[x] == 0):
            b = b + 1
        elif (sentimentslist[x] == -1):
            c = c + 1
    info.append(c)
    info.append(b)
    info.append(a)
    print(info)
    info2 = ['negative', 'neutral','positive']
    plt.bar(info2, info, tick_label=info2, color='#2FC25B')
    plt.show()

if __name__ == '__main__':
    comment = []
    # 输入所需分析的txt
    with open('./bilibiliBius/biliAfter3.10.txt', mode='r', encoding='utf-8') as f:
        rows = f.readlines()
        # print(rows)
        for row in rows:
            if row not in comment:
                comment.append(row.strip('\n'))
        # print(comment)
    snowanalysis(comment)