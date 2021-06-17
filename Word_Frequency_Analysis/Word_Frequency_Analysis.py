import jieba
import numpy as np
import matplotlib.pyplot as plt
import re


txt = open("Word_Frequency_Analysis/笑傲江湖.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

# word = []
# count = []
# for i in range(100):
#     word.append(items[i][0])
#     count.append(items[i][1])
#     print("{0:<5}{1:>5}".format(word[i], count[i]))
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.plot(word[0: 99], count[0: 99])
# plt.xticks(rotation=-90)
# plt.show()

e = re.compile('“[^”]*令狐冲[^”]*？”')
p = e.findall(txt)
for i in range(len(p)):
    print(p[i])
