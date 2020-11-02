#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np

arr = np.array([[1,2,3],[4,5,6]])    
                    

print(arr)
   


# In[11]:


import numpy as np

arr = np.array([[1,2,3],[4,5,6]])    
                    


print("Array is of type: ", type(arr)) 
  
 
print("No. of dimensions: ", arr.ndim) 
  

print("Shape of array: ", arr.shape) 
  
 
print("Size of array: ", arr.size) 


# In[4]:


import numpy as np

a_arr = np.zeros((2,2))   
print(a_arr)              
                      

b_arr = np.ones((1,2))    
print(b_arr)              

  

d_arr = np.eye(2)         
print(d_arr)              
                      

e_arr = np.random.random((2,2))  
print(e_arr)     


# In[12]:


import numpy as np

arr1 = np.arange(0, 30, 5) 
print ( arr1) 
  

arr2= np.linspace(0, 5, 10) 
print ( arr2) 
  
# Reshaping 3X4 array to 2X2X3 array 
arr3 = np.array([[1, 2, 3, 4], 
                [5, 2, 4, 2], 
                [1, 2, 0, 1]]) 
  
newarr = arr3.reshape(2, 2, 3) 
  

print ("Reshaped array:", newarr) 
  
# Flatten array 
arr4 = np.array([[1, 2, 3], [4, 5, 6]]) 
flarr = arr4.flatten() 
  

print ("Fattened array:", flarr) 


# In[17]:


import numpy as np 
  
# An exemplar array 
arr1 = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11,12], 
                [12, 13, 14, 15]]) 
  
# Slicing array 
ans1 = arr1[:1, ::2] 
print((ans1)) 
  
# Integer array indexing example 
ans2 = arr1[[0, 1, 2, 3], [3, 2, 1, 0]] 
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
                                    "(3, 0):\n", ans2) 
  
# boolean array indexing example 
cond = arr > 2 
ans3 = arr[cond] 
print ("Elements greater than 0:", ans3) 


# In[19]:


import numpy as np 
  
arr = np.array([1, 2, 5, 3]) 
  
# add 1 to every element 
print ( arr+1) 
  
# subtract 3 from each element 
print (arr-3) 
  
# multiply each element by 10 
print ( arr*10) 
  
# square each element 
print ( arr**2) 
  


# In[21]:


a = np.array([[1, 2], 
            [3, 4]]) 
b = np.array([[5,6], 
            [7, 8]]) 
  
# add arrays 
print ( a + b) 
  
# multiply arrays (elementwise multiplication) 
print ( a*b) 
  


# In[22]:


import numpy as np

x = np.array([1, 2])  
print(x.dtype)         

x = np.array([1.0, 2.0])   
print(x.dtype) 

x = np.array([1, 2], dtype=np.int64)   
print(x.dtype)


# In[23]:


import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.array([9,10])
d = np.array([11, 12])

# Inner product of vectors
print(a.dot(b))
print(np.dot(a, b))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(c.dot(d))
print(np.dot(c,d))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(a.dot(c))
print(np.dot(b,d))


# In[24]:


import numpy as np 
from matplotlib import pylot as plt

x=np.arrange(1,11)
y=2*x+5

plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,"ob")
plt.show()


# In[ ]:




