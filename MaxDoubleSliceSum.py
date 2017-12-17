
# coding: utf-8

# In[446]:


def max_X(A):
    crash_dummy=0
    max_slice=[0]*len(A)
    for i in range(1,len(A)-2):
        crash_dummy = max(0,crash_dummy+A[i])
        max_slice[i] = crash_dummy
    return max_slice

def max_Y(A):
    crash_dummy=0
    max_slice=[0]*len(A)
    for i in range(len(A)-2, 1, -1):
        
        crash_dummy = max(0, A[i]+crash_dummy)
        max_slice[i] = crash_dummy
    return max_slice

def solution(A):
    X = max_X(A)
    Y = max_Y(A)

    summ=0
    if len(X)==0 or len(Y)==0:
        return 0
    max_slice = 0
    for i in range(0, len(A)-2):
        max_slice = max(max_slice,
                 X[i] + Y[i+2] )
 
    return max_slice

