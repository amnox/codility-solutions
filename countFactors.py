def solution(N):
    # write your code in Python 3.6
    counter = 0
    i = 1
    while i*i<N:
        if N%i==0:
            counter+=2
        i += 1
    if i*i==N:
        counter += 1
    return counter
