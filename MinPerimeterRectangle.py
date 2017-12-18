def solution(N):
    min_peri = 4 if N==1 else 0
    area = N + 0
    i=1
    while i*i<area:
        if area%i==0:
            if(i==1):
                min_peri = 2*(i + area//i)
            else:
                peri = 2*(i + area//i)
                if peri<min_peri:
                    min_peri = peri
        i += 1
    if i*i == area:
        peri = 2*(i + area//i)
        if peri<min_peri:
            min_peri = peri
    
    return min_peri
