
# coding: utf-8

# In[81]:


#right and left
def solution(N):
    rt=[]
    lt=[]
    cass=0
    for i in range(0,len(N)):
        rt.append(N[i]+i)
        lt.append(i-N[i])
    for i in range(0,len(N)-1):
        if cass>10000000:
            return -1
        for j in range(i+1,len(N)):
            if (lt[j]<=rt[i]):
                cass+=1
    return cass
    

