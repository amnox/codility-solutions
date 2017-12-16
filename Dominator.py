def solution(A):
    len_A=len(A)
    if len_A==0:
        return -1
    B=A + []
    B.sort()
    occurrences = B.count(B[int(len_A/2)])
    if occurrences<=len(A)/2:
        return -1
    else: return A.index(B[int(len_A/2)])
