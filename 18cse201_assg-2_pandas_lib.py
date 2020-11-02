#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
#s = pd.Series(Data, index = Index) 
data1 =[1,4,8,6,5,6,10]   
  
ans1 = pd.Series(Data1)     
print(ans1)

 
data2 =['a', 'b', 'c', 'd', 'e', 'f', 'g']  
  

ans2= pd.Series(data1, data2)
print(ans2)


# In[14]:


import pandas as pd

dictionary ={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}  
  
# Creating series of Dictionary type 
dict1= pd.Series(dictionary)  
print(dict1)


# In[16]:


import pandas as pd

data_set=[[2, 3, 4], [5, 6, 7]]   
indx=[1,2]
# Creating series of 2darray 
ans= pd.Series(data_set,indx)

print(ans)


# In[24]:


import pandas as pd 

data1 ={'a':1, 'b':2, 'c':3, 'd':4}    
  
    
data2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9}  
  

grp = {'first':data1, 'second':data2}  
  
# DataFrame  
ans = pd.DataFrame(grp)

print(df)


# In[29]:


import pandas as pd
ans = pd.DataFrame({"a" : [4 ,5, 6],"b" : [7, 8, 9],"c" : [10, 11, 12]},index = [1, 2, 3])
print(ans)


# In[28]:


import pandas as pd 
  

series1 = pd.Series([1, 3, 4, 5, 6, 2, 9])    
  


series2 = pd.Series(['a', 'b', 'c', 'd', 'e','f','g'])      
  
# Define Data 
grp ={'first':series1, 'second':series2, }  
  
# Create DataFrame 
ans = pd.DataFrame(grp)   

print(ans)


# In[32]:


import pandas as pd  
  

arr1 =[[2, 3, 4], [5, 6, 7]]  
  
# Define 2d array 2 
arr2 =[[2, 4, 8], [1, 3, 9]]  
  
# Define Data 
ans ={'first': arr1, 'second': arr2}   
  
# Create DataFrame 
final_ans = pd.DataFrame(ans)  

print(final_ans)


# In[34]:


import numpy as np
ans1 = pd.DataFrame({'name': ['John', 'Smith','Paul'],
                     'Age': ['25', '30', '50']},
                    index=[0, 1, 2])
ans2 = pd.DataFrame({'name': ['Adam', 'Smith' ],
                     'Age': ['26', '11']},
                    index=[3, 4])  


final_ans = pd.concat([ans1,ans2]) 
print(final_ans)


# In[ ]:


import matplotlib as plot
import pandas as pd
ans= pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(ans)
ans.plot.hist() 


# In[ ]:


import matplotlib.pyplot as plt
from pylab import randn
X = randn(200)
Y = randn(200)
plt.scatter(X,Y, color='r')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

