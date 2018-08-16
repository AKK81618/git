
# coding: utf-8

# In[1]:


name = "anna"


# In[2]:


age = 28


# In[3]:


print(name)


# In[4]:


print(age)


# In[5]:


print("my name is")


# In[6]:


print("my name is", name)


# In[7]:


print("my age is", age)


# In[9]:


print("my name is", name,"and my age is", age)


# In[10]:


newage = age - 20


# In[11]:


multipliedage = age * 2


# In[12]:


print("your age is actually", newage)


# In[13]:


print("your multiplied age is", multipliedage)


# In[14]:


sequence = "CTAGCTAG"


# In[15]:


print(sequence)


# In[16]:


print(sequence[0])


# In[17]:


print(sequence[3])


# In[18]:


print("my fourth letter is", sequence[3])


# In[19]:


len(sequence)


# In[20]:


COX1 = "CTAG"


# In[21]:


first_name = "anna"


# In[23]:


sequence[0:2]


# In[24]:


sequence[0:3]


# In[25]:


type(sequence)


# In[26]:


type(age)


# In[27]:


COX2 = "TACG"


# In[28]:


COX1 = "CTAG"


# In[29]:


COX1 + COX2


# In[30]:


firstname = "anna"


# In[31]:


lastname = "k"


# In[32]:


firstname + " " + lastname


# In[33]:


age


# In[34]:


len(age)


# In[35]:


name + age


# In[37]:


5**2


# In[38]:


print("5 square is", 5**2)


# In[39]:


5%2


# In[40]:


# this is a comment


# In[41]:


# adding two sequences because they are the same gene


# In[42]:


COX1 + COX2


# In[43]:


max(23,2,5)


# In[44]:


max(3,"anna")


# In[45]:


round(3.142340983)


# In[46]:


help(round)


# In[47]:


max(21, 32, 45) + min(21, 32, 45)


# In[48]:


hundred_c = "c" * 100


# In[49]:


print(hundred_c)


# In[50]:


hundred_c + COX1


# In[51]:


len(hundred_c +COX1)


# In[52]:


import math


# In[53]:


math.sin(180)


# In[54]:


print("the sine of 180 is", math.cos(180))


# In[55]:


math.pi


# In[56]:


math.sin(math.pi)


# In[57]:


math.cos(math.pi)


# In[58]:


help(math)


# In[59]:


print("sin(pi/2)")


# In[68]:


print("sin(pi/2)=", math.sin(pi/2))


# In[69]:


import math


# In[70]:


print("sin(pi/2)", math.sin(pi/2))


# In[71]:


from math import pi, degrees


# In[72]:


math.sin(pi/2)


# In[73]:


import PANDAS


# In[74]:


import pandas


# In[84]:


pandas.read_csv("C:/Users/AK/Desktop/SWC/python/data/data/gapminder_gdp_oceania.csv")


# In[85]:


data = pandas.read_csv("C:/Users/AK/Desktop/SWC/python/data/data/gapminder_gdp_oceania.csv")


# In[86]:


print(data)


# In[88]:


pandas.read_csv("C:/Users/AK/Desktop/SWC/python/data/data/gapminder_gdp_oceania.csv", inddata = ex_col="country")


# In[89]:


print(data)


# In[90]:


data.info()


# In[91]:


data


# In[92]:


data.T


# In[93]:


data.describe()


# In[94]:


data.T.describe()


# In[95]:


data = pandas.read_csv("C:/Users/AK/Desktop/SWC/python/data/data/gapminder_gdp_americas.csv")


# In[96]:


data2 = pandas.read_csv("C:/Users/AK/Desktop/SWC/python/data/data/gapminder_gdp_americas.csv")


# In[97]:


print(data2)


# In[98]:


data2.describe()


# In[99]:


data2.T.describe()


# In[100]:


data2 = pandas.read_csv("C:/Users/AK/Desktop/SWC/python/data/data/gapminder_gdp_americas.csv", index_col = "country")


# In[101]:


data2


# In[102]:


data2.describe()


# In[103]:


data2.T.describe()


# In[104]:


data.columns


# In[105]:


data2.columns


# In[107]:


data2


# In[108]:


data2.iloc[1,2]


# In[111]:


data2.iloc[0,1]


# In[112]:


data.loc["Peru", "gdpPercap_1957"]


# In[113]:


data = pandas.read_csv("C:/Users/AK/Desktop/SWC/python/data/data/gapminder_gdp_oceania.csv")


# In[114]:


data.loc["Australia",:]


# In[116]:


pandas.read_csv("C:/Users/AK/Desktop/SWC/python/data/data/gapminder_gdp_oceania.csv", index_col="country")


# In[117]:


data.loc[:,"gdpPercap_1962"]


# In[126]:


data.loc[:,"gdpPercap_1952":"gdpPercap_1962"].min()


# In[127]:


subset = data.loc[:,"gdpPercap_1952":"gdpPercap_1962"]


# In[128]:


print(subset>11000)


# In[131]:


subset[subset>11000].describe()


# In[132]:


pandas.read_csv("C:/Users/AK/Desktop/SWC/python/data/data/gapminder_gdp_europe.csv", index_col="country")


# In[134]:


data3 = ("C:/Users/AK/Desktop/SWC/python/data/data/gapminder_gdp_europe.csv")


# In[138]:


data3.loc["Serbia","gdpPercap_2007"]


# In[140]:


data3.loc["Italy":"Norway", "gdpPercap_1962":"gdpPercap_1972"]

