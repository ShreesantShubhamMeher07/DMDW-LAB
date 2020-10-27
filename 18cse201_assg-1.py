#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
l1=list(map(int,input().split()))
sum=0
for i in l1:
    sum+=i
mean_val=sum/len(l1)

l1.sort()

print("mean value is :",mean_val)

if(len(l1)%2 !=0):
    midle_val=len(l1)//2    
    print("median is:",l1[midle_val])
else:
    midle_val=len(l1)//2
    ans=l1[midle_val]+l1[midle_val - 1]
    ans=ans/2
    print("median is:",ans)

max_val=0;
ans=l1[0]
for i in l1:
    cnt=l1.count(i)
    if cnt > max_val :
        max_val=cnt
        ans=i
print("Mode is:",ans)

sum=0;
for i in l1:
    x=mean_val-i
    sum=sum+(x*x)
    
covarience_val=sum/len(l1)

std_dav=math.sqrt(covarience_val)
print("covariance is:",covarience_val)
print("Standard daviation is:",std_dav)

