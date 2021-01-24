import os
import re
import pickle
from wordcloud import WordCloud
# -*- coding: utf-8 -*-
import jieba
import jieba.posseg as pseg

'''词云'''


def drawWordCloud(words, title, savepath='./results'):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    wc = WordCloud(font_path='simkai.ttf', background_color='white', max_words=2000, width=1920, height=1080, margin=5)
    wc.generate_from_frequencies(words)
    wc.to_file(os.path.join(savepath, title + '.png'))


'''统计词频'''


def statistics(texts, stopwords):
    words_dict = {}
    for text in texts:
        temp = jieba.lcut(text)
        for t in temp:
            if t in stopwords or t == "comment" or t == "2020" or t == "info" or t == "time" or t == "\"" or t == "\'" or t == "’" or t == "‘":
                continue
            if t in words_dict.keys():
                words_dict[t] += 1
            else:
                words_dict[t] = 1
    return words_dict


if __name__ == '__main__':
    import argparse

    # parser = argparse.ArgumentParser(description="weibo comments analysis")
    # parser.add_argument('-i', dest='input', help='input file')
    # parser.add_argument('-o', dest='output', help='output file')
    # args = parser.parse_args()
    # input_file = args.input
    # out_file = args.output
    stopwords = open('./numbers.txt', 'r', encoding='utf-8').read().split('\n')[:-1]
    words = open("./CCTVnews/biliAfter3.10.txt", "r", encoding='utf-8').read().split('\n')
    words_dict = statistics(words, stopwords)
    drawWordCloud(words_dict, "./Figure_3", savepath='./bilibiliResults')
