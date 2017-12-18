def peak_calc(N):
    remainder = len(N)%3
    peaks = []
    array_len=len(N)
    for i in range(0,array_len,2):
        if i==0:
            continue
        if remainder == 0 or remainder==2:
            
            if (i+1)==(array_len-1):
                if (N[i])>(N[i-1]) and (N[i])>(N[i+1]):
                    peaks+=[i]
        if (N[i-1])>(N[i-2]) and (N[i-1])>(N[i]):
            peaks+=[i-1]
    return peaks

def flag_fits(flags,peaks):
    counter = 0
    remaining_flags = flags
    last_flag = peaks[0]
    mot = False
    while remaining_flags!=0:
        if counter==(len(peaks)):
            break
        if counter==0:
            counter += 1
            remaining_flags -= 1
            continue
        if abs(last_flag-peaks[counter])<flags:
            counter += 1
            continue
        elif abs(last_flag-peaks[counter])>=flags:
            last_flag=peaks[counter]
            counter += 1
            remaining_flags -= 1
            continue
            
            
    return remaining_flags==0

def solution(A):
    peaks = peak_calc(A)
    ans = 0
    for i in range(len(peaks),0,-1):
        print i
        if flag_fits(i,peaks):
            ans =i
            break
    return ans
