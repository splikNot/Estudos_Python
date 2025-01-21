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

#Abre o Arquivo da Alice
alice = open('AliceInWonderland.txt','r', encoding = 'utf8')
raw = alice.read()


#cria um tokenizer
tokenizer = nk.tokenize.RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(raw)# A variavel token é uma lista de tokens

alice_lwords = []
for word in tokens: #transformando toda as letras em minusculas
    alice_lwords.append(word.lower())
    


alice_words_ns = []
for word in alice_lwords: #Cria lista das palavras sem as SW's
    if word not in sw:
        alice_words_ns.append(word)
        
#Cria o dicfreq_Alice
dicfreq_alice = {'a':{},'b':{},'c':{},'d':{},'e':{},'f':{},'g':{},'h':{},'i':{},'j':{},'k':{},"l":{},'m':{},'n':{},'o':{},'p':{},'q':{},'r':{},'s':{},'t':{},'u':{},'v':{},'w':{},'x':{},'y':{},'z':{}}
for word in alice_words_ns:
    inic = (word[0])
    if inic not in dicfreq_alice:
        alice_words_ns.remove(word)
    elif word in dicfreq_alice[inic]:
        count = dicfreq_alice[inic][word]
        count+=1
        dicfreq_alice[inic][word] = count
        
    else:
        dicfreq_alice[inic].update([(word , 1)])
        
     
lwordena_alice= []
keys_alice = []
#cria lista de pares dicionários
for i in dicfreq_alice:
    for word in dicfreq_alice[i]:
        keys_alice.append(word)
        temp = {}
        temp[word] = dicfreq_alice[i][word]
        lwordena_alice.append(temp)

#ordenação        
ordena(lwordena_alice,keys_alice)

final_alice = []
for i in range(20):
    for word in lwordena_alice[i]:
        value = lwordena_alice[i][word]
        
    
    
    temp = (word), value
    final_alice.append(temp)
    
    
    

freqword = pd.DataFrame.from_records(final_alice, columns=['word','count'])
freqword.plot(kind= 'bar', x = 'word')

wordc = wd.WordCloud(width=900,height=500, max_words=20,\
relative_scaling=1,normalize_plurals=False).generate_from_frequencies(dict(final_alice))
plt.figure()
plt.imshow(wordc, interpolation='bilinear')
plt.axis('off')
plt.show()
