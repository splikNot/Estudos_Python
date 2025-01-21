# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:27:56 2020

@author: Raphael
"""
import pandas as pd
import matplotlib.pyplot as plt
import nltk as nk
from nltk.corpus import stopwords
import wordcloud as wd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

sw = nk.corpus.stopwords.words('english')

def ordena(a,b):
    for i in range(1,len(a)):
        temp , temp2, temp3 = a[i][b[i]], a[i], b[i] 
        j=i
        while j>0 and temp > a[j-1][b[j-1]]:
            a[j], b[j] = a[j-1], b[j-1]
            j-=1
            a[j], b[j] = temp2, temp3
    return a

#Abre o arquivo do Alice atráves do espelho
ttlg = open('ThroughTheLookingGlass.txt','r',encoding = 'utf8')
raw = ttlg.read()

tokenizer = nk.tokenize.RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(raw)
ttlg_lwords = []
for word in tokens:
    ttlg_lwords.append(word.lower())


ttlg_words_ns = []
for word in ttlg_lwords:
    if word not in sw:
        ttlg_words_ns.append(word)

#Cria o dicfreq_ttlg
dicfreq_ttlg = {'a':{},'b':{},'c':{},'d':{},'e':{},'f':{},'g':{},'h':{},'i':{},'j':{},'k':{},"l":{},'m':{},'n':{},'o':{},'p':{},'q':{},'r':{},'s':{},'t':{},'u':{},'v':{},'w':{},'x':{},'y':{},'z':{}}
for word in ttlg_words_ns:
    inic = word[0]
    if inic not in dicfreq_ttlg:
        ttlg_words_ns.remove(word)
    elif word in dicfreq_ttlg[inic]:
        count = dicfreq_ttlg[inic][word]
        count += 1
        dicfreq_ttlg[inic][word] = count
    else:
        dicfreq_ttlg[inic].update([(word,1)])
        
lwordena_ttlg = []
keys_ttlg = []

for i in dicfreq_ttlg:
    for word in dicfreq_ttlg[i]:
        keys_ttlg.append(word)
        temp = {}
        temp[word] = dicfreq_ttlg[i][word]
        lwordena_ttlg.append(temp)

ordena(lwordena_ttlg,keys_ttlg)

final_ttlg = []
for i in range(20):
    for word in lwordena_ttlg[i]:
        value = lwordena_ttlg[i][word]
        temp = ((word), value)
    final_ttlg.append(temp)
    
freqword = pd.DataFrame.from_records(final_ttlg, columns=['word','count'])
freqword.plot(kind= 'bar', x = 'word')

wordc = wd.WordCloud(width=900,height=500, max_words=20,\
relative_scaling=1,normalize_plurals=False).generate_from_frequencies(dict(final_ttlg))
plt.figure()
plt.imshow(wordc, interpolation='bilinear')
plt.axis('off')
plt.show()
        
        
        
