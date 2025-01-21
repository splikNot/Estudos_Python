# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:30:20 2020

@author: Raphael
"""


import pandas as pd
import matplotlib.pyplot as plt
import nltk as nk
from nltk.corpus import stopwords
import wordcloud as wd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# seta o NLTK para encontrar as stopwords em inglês
sw = nk.corpus.stopwords.words('english')

#Função de ordenção que recebe como parâmetro duas listas
#Uma lista de dicionarios e outra lista com as keys destes dicionarios
def ordena(a,b):
    for i in range(1,len(a)):
        temp , temp2, temp3 = a[i][b[i]], a[i], b[i] 
        j=i
        while j>0 and temp > a[j-1][b[j-1]]:
            a[j], b[j] = a[j-1], b[j-1]
            j-=1
            a[j], b[j] = temp2, temp3
    return a

wep = open('WarAndPeace.txt','r',encoding = 'utf8')
raw = wep.read()

tokenizer = nk.tokenize.RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(raw)
wep_lwords = []
for word in tokens:
    wep_lwords.append(word.lower())
    
wep_words_ns = []
for word in wep_lwords:
    if word not in sw:
        wep_words_ns.append(word)
        
#Inicializa o dicfreq
dicfreq_wep = {'a':{},'b':{},'c':{},'d':{},'e':{},'f':{},'g':{},'h':{},'i':{},'j':{},'k':{},"l":{},'m':{},'n':{},'o':{},'p':{},'q':{},'r':{},'s':{},'t':{},'u':{},'v':{},'w':{},'x':{},'y':{},'z':{}}
for word in wep_words_ns:
    inic = word[0]
    if inic not in dicfreq_wep:
        wep_words_ns.remove(word)
        
    elif word in dicfreq_wep[inic]:
        count = dicfreq_wep[inic][word]
        count+=1
        dicfreq_wep[inic][word] = count
    else:
        dicfreq_wep[inic].update([(word,1)])
        
lwordena_wep = []
keys_wep = []
for i in dicfreq_wep:
    for word in dicfreq_wep[i]:
        keys_wep.append(word)
        temp = {}
        temp[word] = dicfreq_wep[i][word]
        lwordena_wep.append(temp)

ordena(lwordena_wep,keys_wep)

final_wep = []
for i in range(20):
    for word in lwordena_wep[i]:
        value = lwordena_wep[i][word]
        temp = ((word), value)
    final_wep.append(temp)

freqword = pd.DataFrame.from_records(final_wep, columns=['word','count'])
freqword.plot(kind= 'bar', x = 'word')

wordc = wd.WordCloud(width=900,height=500, max_words=20,\
relative_scaling=1,normalize_plurals=False).generate_from_frequencies(dict(final_wep))
plt.figure()
plt.imshow(wordc, interpolation='bilinear')
plt.axis('off')
plt.show()
