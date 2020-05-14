#!/usr/bin/env python
# coding: utf-8

# In[529]:


import re


# In[531]:


i = 1996
lists = []
while i<=2020:
    f = open("files/"+str(i)+".txt",'r',encoding="utf-8")
    divs = f.readlines()
    
    flag = 0
    newLineCheck = 0
    for div in divs:
        if len(div)==1: newLineCheck = 1
        else: newLineCheck = 0
        if flag == 1:
            if newLineCheck == 1:
                lists.append(str(div))
            if newLineCheck == 0:
                lists[len(lists)-1] = lists[len(lists)-1]+ ' ' + str(div)
        if "TITLE and AUTHOR" in div:
            flag = 1
            
    i = i + 1


# In[532]:


print(len(lists))
i = 0;
for l in lists:
    if "[Languages:" in l or "[Language:" in l:
        del lists[i]
    i = i+1


# In[533]:


i = 0
for l in lists:
    lists[i] = re.sub(r'\n','',l)
    i = i + 1
    
i = 0
for l in lists:
    lists[i] = re.sub(r'\s\s\s*\d+','',l)
    i = i + 1
    
i = 0
for l in lists:
    lists[i] = re.sub(r'\[.*\]','',l)
    i = i + 1


# In[534]:


len(lists)


# In[535]:


book = []
author = []
for l in lists:
    s = l.strip()
    s = s.split('by')
    book.append(s[0])
    if(len(s)==1):
        author.append("N/A")
    else:
        author.append(s[1])


# In[537]:


import csv
i = 0
with open('booksAndAuthors.csv','w',newline='',encoding="utf-8") as file:
    c = csv.writer(file)
    c.writerow(["ID", "Book_Name", "Author"])
    while i<len(book):
        c.writerow([i,book[i].strip(),author[i].strip()])
        i = i + 1


# In[ ]:




