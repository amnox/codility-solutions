def peak_calc(N):
    indices = []
    for i in range(0,len(N)):
        if (i+2)>(len(N)-1):
            break
        if N[i+1]>N[i] and N[i+1]>N[i+2]:
            indices+=[i+1]
    return indices
def factor(n):
    factors = list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    return factors[0:len(factors)-1]
def solution(A):
    len_arr = len(A)
    peaks = peak_calc(A)
    generic = range(0,len_arr)
    factors = factor(len_arr)
    boss = 0
    for i in factors:
        passed = False
        items_in_each = len_arr//i
        number_of_arrays = len_arr//items_in_each
        splits = range(0,len_arr+1,items_in_each)
        #print "Printing for {}".format(i)
        for j in range(0,len(splits)-1): 
            #print list(set(generic[splits[j]:splits[j+1]]) & set(peaks))
            if len(list(set(generic[splits[j]:splits[j+1]]) & set(peaks)))==0:
                break
            if j==len(splits)-2:
                passed = True
            pass
        if passed == True:
            if boss<i:
                boss = i
    return boss
