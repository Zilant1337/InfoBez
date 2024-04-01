import math
import time
from datetime import datetime, timedelta
import numpy as np
def GCD (a,b):
    if(b<0):
        b=-b
    if(a<0):
        a=-a
    if(b>a):
        return(GCD(b,a))
    if(b==0):
        return
    if(a%b==0):
        return b
    else:
        return GCD(b,a%b)

def GCD2(a,b):
    A = float(a)
    B = float(b)
    if(A%1!=0):
        A=A**-1
    if(B%1!=0):
        B=b**-1
    if(A<B):
        A,B=B,A
    divList=[]
    while(A%B!=0):
        temp=A
        divList.append(A//B)
        A=B
        B=temp%B
    x=0
    y=B
    while(len(divList)!=0):
        temp=x
        x=y
        y=temp-(y*divList.pop())
    return GCD(x,y)
def mod (a,powA,b):
    return (a**powA%b)

def ReverseCipher(string):
    return string[::-1]

# print(GCD2(-7**2*-7,30))
print(ReverseCipher("Hello"))