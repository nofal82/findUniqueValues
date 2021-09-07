#!/usr/bin/env python
# coding: utf-8

# In[5]:


training_data = [['Green', 3, 'Mango'], 
                ['Yellow', 3 , 'Mango'],
                ['Red', 1, 'Grape'],
                ['Red', 1, 'Grape'],
                ['Yellow', 3 , 'Lemon']]
training_data


# In[8]:


# column label
# these are used only to print the tree
header = ["color", "diameter", "label"]
def unique_vals(rows, col):
    """find unique valaues for the column in a dataset"""
    return set([row[col] for row in rows])


unique_vals(training_data, 2)


# In[11]:


def class_counts(rows):
    """count the number of each type of example in a dataset"""
    counts = {} # a dictionary of label -> count.
    for row in rows:
        # in our dataset format the label table is always the last column
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


class_counts(training_data)
    


# In[16]:


def is_numeric(value):
    """test if the value is numeric"""
    return isinstance(value, int) or isinstance(value, float)

is_numeric(3.4)


# In[ ]:




