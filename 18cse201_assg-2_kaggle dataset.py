#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


iris=pd.read_csv("iris.csv")


# In[6]:


iris


# In[7]:


iris.shape


# In[8]:


iris.columns


# In[9]:


iris['Species'].value_counts()


# In[10]:


iris['Species'].count()


# In[11]:


iris.plot(kind="scatter",x="SepalLengthCm",y="SepalWidthCm")
plt.show()


# In[12]:


sns.set_style("whitegrid");
sns.FacetGrid(iris,hue="Species",size=4).map(plt.scatter,"SepalLengthCm","SepalWidthCm").add_legend()
plt.show()


# In[13]:


plt.close()
sns.set_style("whitegrid")
sns.pairplot(iris,hue="Species",height=3)
plt.show()


# In[14]:


iris_setosa=iris.loc[iris["Species"]=="Iris-setosa"]
iris_vesicolour=iris.loc[iris["Species"]=="Iris-versicolor"]
iris_verginica=iris.loc[iris["Species"]=="Iris-virginica"]
plt.plot(iris_setosa["PetalLengthCm"],np.zeros_like(iris_setosa['PetalLengthCm']),'o',label="setosa")
plt.plot(iris_vesicolour["PetalLengthCm"],np.zeros_like(iris_setosa['PetalLengthCm']),'o',label="vericolour")
plt.plot(iris_verginica["PetalLengthCm"],np.zeros_like(iris_setosa['PetalLengthCm']),'o',label="verginica")
plt.legend()
plt.show()
# plt.plot(iris_setosa,np.zeroes_like)


# In[15]:


sns.FacetGrid(iris,hue="Species",height=5).map(sns.distplot,"PetalLengthCm").add_legend()


# In[16]:


sns.FacetGrid(iris,hue="Species",height=5).map(sns.distplot,"PetalWidthCm").add_legend()


# In[17]:


sns.FacetGrid(iris,hue="Species",height=5).map(sns.distplot,"SepalWidthCm").add_legend()


# In[18]:


sns.FacetGrid(iris,hue="Species",height=4).map(sns.distplot,"SepalLengthCm").add_legend()


# In[27]:


counts ,bin_edges=np.histogram(iris_setosa["PetalLengthCm"],bins=10,density=True)
# print(counts)
# print(bin_edges)
# print(bin_edges[1:])
pdf=counts/sum(counts)
cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf,label="pdf_iris_setosa")#
plt.plot(bin_edges[1:],cdf,label="cdf_iris_setosa")
plt.legend();
counts ,bin_edges=np.histogram(iris_vesicolour["PetalLengthCm"],bins=10,density=True)
# print(counts)
# print(bin_edges)
# print(bin_edges[1:])
pdf=counts/sum(counts)
cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf,label="pdf_iris_setosa")#
plt.plot(bin_edges[1:],cdf,label="cdf_iris_setosa")
plt.legend();
counts ,bin_edges=np.histogram(iris_verginica["PetalLengthCm"],bins=10,density=True)
# print(counts)
# print(bin_edges)
# print(bin_edges[1:])
pdf=counts/sum(counts)
cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf,label="pdf_iris_setosa")#
plt.plot(bin_edges[1:],cdf,label="cdf_iris_setosa")
plt.legend();


# In[39]:


counts,bins=np.histogram(iris_setosa["PetalLengthCm"],bins=10,density=True)
plt.hist(counts,bins=[0,10,20,30,40,50,60,70,80])
# counts,bins=np.histogram(iris_vesicolour["PetalLengthCm"],bins=10,density=True)
# plt.hist(bins[1:],counts,label="versicolu_petal_length")
# counts,bins=np.histogram(iris_verginica["PetalLengthCm"],bins=10,density=True)
# plt.hist(bins[1:],counts,label="verginca_petal_length")
plt.show()




#TRIAL ONE **************************************************************************************************************


# In[20]:


counts ,bin_edges=np.histogram(iris["PetalLengthCm"],bins=10,density=True)
pdf=counts/sum(counts)
cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)#
plt.plot(bin_edges[1:],cdf)


# # MEAN , STANDARD DEVIATION AND VARIANCE CALCULATION 

# In[21]:


print(np.mean(iris_setosa["PetalLengthCm"]))
print("mean with an out-lier")
print(np.mean(np.append(iris_setosa["PetalLengthCm"],50)))
print(np.mean(iris_vesicolour["PetalLengthCm"]))
print(np.mean(iris_verginica["PetalLengthCm"]))

print("standard deviations are:")
print(np.std(iris_setosa["PetalLengthCm"]))
print(np.std(iris_vesicolour["PetalLengthCm"]))
print(np.std(iris_verginica["PetalLengthCm"]))


# # MEDIAN CALCULATION

# In[22]:


print(np.median(iris_setosa["PetalLengthCm"]))
print("median with an out-lier")
print(np.median(np.append(iris_setosa["PetalLengthCm"],50)))
print(np.median(iris_vesicolour["PetalLengthCm"]))
print(np.median(iris_verginica["PetalLengthCm"]))


# # PERCENTILES AND QUANTILES

# In[23]:


print("90th percentile")
print(np.percentile(iris_setosa["PetalLengthCm"],90))
print("the quantiles are :->")
print(np.percentile(iris_setosa["PetalLengthCm"],np.arange(25, 125, 25)))


# # MEADIAN ABSOLUTE DEVIATION AND IQR(INTER QUARTILR RANGE)

# In[24]:


from statsmodels import robust
print(robust.mad(iris_setosa["PetalLengthCm"]))
print(robust.mad(iris_vesicolour["PetalLengthCm"]))
print(robust.mad(iris_verginica["PetalLengthCm"]))


# In[44]:


sns.set_style("darkgrid")
sns.FacetGrid(iris,hue="Species",height=6).map(plt.scatter,"PetalLengthCm","PetalWidthCm")


# # MULTIVARIATE PROBABILITY DENSITY FUNCTION

# In[49]:


sns.jointplot(x="PetalLengthCm",y="PetalWidthCm",data=iris_setosa,kind="kde")
plt.show()


# In[ ]:




