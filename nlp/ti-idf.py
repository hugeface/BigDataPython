# 用 TF-IDF 求 Item Weight
import os
import math

file_path = './data'

i = 0
# 获取doc和对应每篇文章的词频
doc_words = dict()
for filename in os.listdir(file_path):
    if i % 100 == 0:
        print(i, 'files loaded!!')
        # break
    with open(file_path + '/' + filename, 'r', encoding='utf-8') as f:
        word_freq = dict()
        for line in f.readlines():
            words = line.strip().split(' ')
            for word in words:
                if len(word.strip()) < 1:
                    continue
                if word_freq.get(word, -1) == -1:
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1
    doc_words[filename] = word_freq
    i += 1
doc_nums = float(i)
# print(doc_words)

# 统计每个词的doc-freq
doc_freq = {}
for doc in doc_words.keys():
    for word in doc_words[doc].keys():
        if doc_freq.get(word, -1) == -1:
            doc_freq[word] = 1
        else:
            doc_freq[word] += 1
print(doc_freq)

# idf 公式
for word in doc_freq.keys():
    doc_freq[word] = math.log(doc_nums / float(doc_freq[word] + 1))
print(doc_freq)

# tf * idf
print(doc_words['5yule.seg.cln.txt'].get('毒'))
for doc in doc_words.keys():
    for word in doc_words[doc].keys():
        doc_words[doc][word] *= doc_freq[word]
print(doc_words['5yule.seg.cln.txt'].get('毒'))