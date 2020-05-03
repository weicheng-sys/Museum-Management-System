# -*- coding = utf-8 -*-
# @Time : 2020/4/27 16:03
# @Author : surpass-slowly
from collections import defaultdict
import pymysql
import jieba
import codecs


def seg_word(sentence):
    """使用jieba对文档分词"""
    seg_list = jieba.cut(sentence)
    seg_result = []
    for w in seg_list:
        seg_result.append(w)
    # 读取停用词文件
    stopwords = set()
    fr = codecs.open('D:\Python\web_crawler\MuseumNews\\analysis\stopwords.txt', 'r', 'utf-8')
    for word in fr:
        stopwords.add(word.strip())
    fr.close()
    # 去除停用词
    return list(filter(lambda x: x not in stopwords, seg_result))


def classify_words(word_dict):
    """词语分类,找出情感词、否定词、程度副词"""
    # 读取情感字典文件
    sen_file = open('D:\Python\web_crawler\MuseumNews\\analysis\emotion.txt', 'r+', encoding='utf-8')
    # 获取字典文件内容
    sen_list = sen_file.readlines()
    # 创建情感字典
    sen_dict = defaultdict()
    # 读取字典文件每一行内容，将其转换为字典对象，key为情感词，value为对应的分值
    for s in sen_list:
        # 每一行内容根据空格分割，索引0是情感词，索引1是情感分值
        s_split = s.split(' ')
        if len(s_split) == 2:
            sen_dict[s.split(' ')[0]] = s.split(' ')[1]

    # 读取否定词文件
    not_word_file = open('D:\Python\web_crawler\MuseumNews\\analysis\\negator.txt', 'r+', encoding='utf-8')
    # 由于否定词只有词，没有分值，使用list即可
    not_word_list = not_word_file.readlines()

    # 读取程度副词文件
    degree_file = open('D:\Python\web_crawler\MuseumNews\\analysis\\adverb.txt', 'r+', encoding='utf-8')
    degree_list = degree_file.readlines()
    degree_dic = defaultdict()
    # 程度副词与情感词处理方式一样，转为程度副词字典对象，key为程度副词，value为对应的程度值
    for d in degree_list:
        d_split = d.split(' ')
        if len(d_split) == 2:
            degree_dic[d.split(' ')[0]] = d.split(' ')[1]

    # 分类结果，词语的index作为key,词语的分值作为value，否定词分值设为-1
    sen_word = dict()
    not_word = dict()
    degree_word = dict()

    # 分类
    for word in word_dict.keys():
        if word in sen_dict.keys() and word not in not_word_list and word not in degree_dic.keys():
            # 找出分词结果中在情感字典中的词
            sen_word[word_dict[word]] = sen_dict[word]
        elif word in not_word_list and word not in degree_dic.keys():
            # 分词结果中在否定词列表中的词
            not_word[word_dict[word]] = -1
        elif word in degree_dic.keys():
            # 分词结果中在程度副词中的词
            degree_word[word_dict[word]] = degree_dic[word]
    sen_file.close()
    degree_file.close()
    not_word_file.close()
    # 将分类结果返回
    return sen_word, not_word, degree_word


def list_to_dict(word_list):
    """将分词后的列表转为字典，key为单词，value为单词在列表中的索引，索引相当于词语在文档中出现的位置"""
    data = {}
    for x in range(0, len(word_list)):
        data[word_list[x]] = x
    return data


def socre_sentiment(sen_word, not_word, degree_word, seg_result):
    """计算得分"""
    # 权重初始化为1
    W = 1
    score = 0
    # 遍历分词结果
    for i in range(0, len(seg_result)):
        # 若是程度副词
        if i in degree_word.keys():
            W *= degree_word[i]
        # 若是否定词
        elif i in not_word.keys():
            # print(i)
            W *= -1
        elif i in sen_word.keys():
            score += float(W) * float(sen_word[i])
            W = 1
    return score


# 计算得分
def setiment_score(sententce):
    # 1.对文档分词
    seg_list = seg_word(sententce)
    # 2.将分词结果列表转为dic，然后找出情感词、否定词、程度副词
    sen_word, not_word, degree_word = classify_words(list_to_dict(seg_list))
    # 3.计算得分
    score = socre_sentiment(sen_word, not_word, degree_word, seg_list)
    return score


def analysis_content(content):
    ana = setiment_score(content)
    if ana >= 10:
        return '正面新闻'
    else:
        return '负面新闻'
