# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 06:50:35 2020

@author: Yuzhe Huang
"""

#1
##(a)
print(list(range(1,21)))
##(b)
print(list(reversed(range(1,21))))
##(c)
print(list(range(1,21))+list(reversed(range(1,20))))
##(d)
print([4,6,3]*10)
##(e)
mylist=[4,6,3]*10
mylist.append(4)
print(mylist)


#2
import math
x=3
alist=[]
while x<=6:
      y=math.exp(x)*math.cos(x)
      alist.append(y)
      x=x+0.1

print(alist)

#3
a=1
blist=[]
while a<=25:
    b=math.pow(2,a)/a
    blist.append(b)
    a=a+1

print(blist)


#4
##(a)
clist=list(range(1,21))
dlist=[]
n=0
while n<=19:
    m=19-n
    c=clist[n]-clist[m]
    dlist.append(c)
    n=n+1

print(dlist)
    

##(b)
elist=[]
for x in clist:
    if x%2==0:
        d="True"
    else:
        d="False"
    elist.append(d)

print(elist)

#5
# Change working directory
import os
os.getcwd()
os.chdir("C:/Users/huang/Desktop/BU/python")

##(a)
with open('lorem.txt','r') as file:
    count_14=0
    content=file.read()
    str_vals = content.split(' ')
    for i in str_vals:
        if len(i)>=1 and len(i)<=4:
            count_14+=1

print(count_14)

with open('lorem.txt','r') as file:
    count_47=0
    content=file.read()
    str_vals = content.split(' ')
    for i in str_vals:
        if len(i)>4 and len(i)<=7:
            count_47+=1

print(count_47)

with open('lorem.txt','r') as file:
    count_8=0
    content=file.read()
    str_vals = content.split(' ')
    for i in str_vals:
        if len(i)>=8:
            count_8+=1

print(count_8)



##(b)
with open('lorem.txt','r') as file:
    count=0
    content=file.read()
    for i in content:
        if i.isupper():
            count+=1

print(count)












