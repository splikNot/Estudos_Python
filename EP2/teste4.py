#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:28:12 2018

@author: maruyama
"""
from heapq import heappush, heappop
from teste3 import Node

def main():
  # cria objetos do tipo Node. O numero inteiro se refere a frequencia
  a=Node('a',9)
  b=Node('b',2)
  c=Node('c',4)
  d=Node('d',4)
  e=Node('e',3)

  h=[]  # cria uma lista vazia
  # coloca cada objto Node na lista h[]
  # heap e' indexada pelo primeiro elemento *.frequencia
  heappush(h,(d.frequencia,d))
  heappush(h,(a.frequencia,a))
  heappush(h,(b.frequencia,b))
  heappush(h,(e.frequencia,e))
  heappush(h,(c.frequencia,c))
  # apos estas insercoes a lista h[] nao se encontra ordenada 
  # nas operacoes de heappop o elemento retirado e' o
  # com menor valor de frequencia
  while len(h) is not 0: # ale a lista ficar vazia
      x = heappop(h)
      print('frequencia = ',x[0],' -> caracter = ',x[1].caracter)
      # lembre-se que x[1] e' um objeto do tipo Node
         
if __name__ == "__main__": main()  
