
# coding: utf-8

# In[242]:


def solution(A):
    maxlist=0
    for i in range(0,len(A)):
        contender=max(A[i:len(A)])-A[i]
        if (maxlist<contender):
            maxlist=contender
    return maxlist

