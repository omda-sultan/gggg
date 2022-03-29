#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("omda")


# In[2]:


st='omda'
i=19
print(st)
print(i)


# In[3]:


st
i


# In[4]:


my_num=22
if my_num>22:
    print("greater than 22")
elif my_num<22:
    print("smaler than 22")
else:
    print("equal 22")


# In[5]:


s_names = ['Alice', 'Bob', 'Carol', 'Dave']
s_names[1]


# In[6]:


s_names[3]


# In[7]:


s_names[-1]


# In[8]:


s_names[1:3]


# In[9]:


s_names[2:]


# In[10]:


s_names[:2]


# In[11]:


s_names.append('omda')


# In[12]:


s_names


# In[13]:


s_names.insert(2,'ali')
s_names


# In[14]:


del s_names[2]
s_names


# In[15]:


for name in s_names:
    print('Hello' + name + ' . ')


# In[16]:


l_n = []
for name in s_names:
    if len(name) > 4:
        l_n.append(name)

l_n


# In[17]:


s_p = []
for name_0 in s_names:
    for name_1 in s_names:
        s_p.append((name_0,name_1))
s_p


# In[19]:


s_p[1]


# In[20]:


s_g = ('omda', 'english', 'A-')
s_g


# In[21]:


s_g.append("assuit")


# In[22]:


s_g = ('omda', 'english', 'A-')
name,lang,gba=s_g
print(name)
print(lang)
print(gba)


# In[23]:


s_g = [
    ('omda', 'Spanish', 'A'),
    ('ali', 'French', 'C'),
    ('moh', 'Italian', 'B+'),
    ('fathy', 'Italian', 'A-'),
]
for name, su, g in s_g:
    if g.startswith('A'):
        print('Congratulations', name,
              'on getting an', g,
              'in', su)


# In[24]:


f_l = {
    'omda': 'Spanish',
    'ali': 'French',
    'saad': 'Italian',
    'fathy': 'Italian',
}
f_l['omda']


# In[25]:


'ali' in f_l


# In[26]:


'aa' in f_l


# In[27]:


f_l["fady"]='dss'
f_l


# In[28]:


for k in f_l:
    v = f_l[k]
    print(k, 'is taking', v)


# In[29]:


s_g = [
    ('ali', 'Spanish', 'A'),
    ('omda', 'French', 'C'),
    ('saad', 'Italian', 'B+'),
    ('fathy', 'Italian', 'A-'),
]
s_g[1]


# In[30]:


s_g[1][2]


# In[ ]:




