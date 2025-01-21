#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:46:12 2018

@author: maruyama
"""

class Node:
    def __init__(self, car=None,freq=None,left=None,right=None):
        self.caracter = car
        self.frequencia = freq
        self.left = left
        self.right = right
    
    def __str__(self):
        if (self.caracter is None):
            return('0')
        else:
            return('1')
        
    def __lt__(self,other):
        if (self.frequencia <= other.frequencia):
            return(True)
        else:
            return(False)
            
class BST:
    def __init__(self,root=None):
        self.root = root
        
    def devolveroot(self):
        return self.root
    
    def preordertraverse(self,p):
        if(p is not None):
            if (p.caracter is not None):
                print(p,end='')
            else:
                print(p,end='')
                self.preordertraverse(p.left)
                self.preordertraverse(p.right)
            
def main():
  a=Node('a',1)
  b=Node('b',3)
  c=Node(None,4,a,b)
  d=Node('d',3)
  e=Node(None,7,d,c)
  x=BST(e)
  p=x.devolveroot()
  x.preordertraverse(p)

if __name__ == "__main__": main()        
            
            
