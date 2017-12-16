
# coding: utf-8

# In[147]:


def goldenLeader(A):
    n = len(A)
    size = 0
    for k in xrange(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in xrange(n):
        if (A[k] == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate
    return leader

def solution(A):
    count=0
    for i in range(0,len(A)-1):
        arr1=A[0:i+1]
        leader1=goldenLeader(arr1)
        if leader1==-1:
            continue
        arr2=A[i+1:len(A)]
        leader2=goldenLeader(arr2)
        if leader2==-1:
            continue
        if leader1==leader2:
            count+=1
        #print 'arr1:{} || arr2:{}'.format(arr1,arr2)
        #print 'arr1:{} || arr2:{}'.format(goldenLeader(arr1),goldenLeader(arr2))
    return count

