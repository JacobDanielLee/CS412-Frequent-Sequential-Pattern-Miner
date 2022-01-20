#!/usr/bin/env python
# coding: utf-8

# # Frequent Sequential Pattern Algorithm
# 
# 

# In[21]:


import sys

#GSP Aprior algorithm
def get_sequences(filename, minimumSupport):
    sequences = readfile(filename)
    
    #Scan DB to find “length-1” candidate sequences
    candidate_one = first_pass(minimumSupport, sequences)
    
    #Scan DB to find “length-1” frequent sequences
    frequent_one = find_frequent(minimumSupport, candidate_one)
    
    #Add frequent length-1 sequences to return
    returnsequences = frequent_one
    
    frequent_k = frequent_one
    
    #Generate “length-(k+1)” candidate sequences from “length-k” frequent sequences using Apriori
    k = 2
    while len(frequent_k) > 0:
        #Generate Candidates
        candidate_k = candidate_generate(frequent_k, k, sequences, candidate_one)
        #Generate frequent sequences
        frequent_k = find_frequent(minimumSupport, candidate_k)
           
        returnsequences.update(frequent_k)    
        
        k += 1
        

    return returnsequences


# In[22]:


def readfile(name):
    sequences = []
    temp = []
    with open(name, "r") as reader:
        lines = reader.readlines()
        #Separate text by space
        for line in lines:
            x = line.strip().split(' ')
            temp.append(x)
        for item in temp:
            for j in item:
                if '<' in j:
                    #Check every relevant <> transaction and add to return WITHOUT BRACKETS
                    subs = j[1:-1]
                    sequences.append(subs)
    return sequences


# In[23]:


def find_frequent(minsupport, d):
    return_dict = {}
    for key in d.keys():
        if d.get(key) >= minsupport:
            return_dict[key] = d.get(key)
    return return_dict


# In[24]:


def first_pass(minsupport, db):
    c1_dict = {}
    for line in db:
        for letter in line:
            if letter not in c1_dict:
                c1_dict[letter] = 0
                
    for i in c1_dict.keys():
        for j in db: 
            if i in j:
                c1_dict[i] += 1
    return c1_dict


# In[27]:


def candidate_generate(freqset, k, seq, c_1):
    candidate_dict = {}
    #Generate Candidates
    for i in freqset.keys():
        for j in c_1.keys():
            if len(i + j) == k:
                var = i + j
                candidate_dict[var] = 0
                        
    #Generate support
    for i in candidate_dict.keys():
        for j in seq:
            #temp = 0
            #count = 0
            #while count < k:
            if i in j:
                candidate_dict[i] = candidate_dict.get(i) + 1
                #if i[count] in j[temp:]:
                    #temp += j[temp:].find(i[count]) + 1
                    #if count == k-1:
                      #  candidate_dict[i] = candidate_dict.get(i) + 1
                #count += 1
                #else:
                    #break
    return candidate_dict


# In[ ]:




