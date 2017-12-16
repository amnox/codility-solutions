def collision(A,B):
    if A==1 and B==0:
        return True
    else:
        return False
def solution(A,B):
    new_pond=[]
    for i in range(0,len(A)):
        if i==0:
            new_pond = [(B[i],A[i]),]
        else:
            new_fish = (B[i],A[i])
            if collision(new_pond[len(new_pond)-1][0],new_fish[0]):
                print "BOOM"
                while 1==1:
                    
                    if len(new_pond)==0:
                        print "New Pond Reset : {}".format(i)
                        new_pond=[new_fish,]
                        break
                    elif new_pond[len(new_pond)-1][0]==new_fish[0]:
                        print "equal"
                        new_pond+=[new_fish,]
                        break
                    elif new_pond[len(new_pond)-1][1]>new_fish[1]:
                        break
                    elif new_pond[len(new_pond)-1][1]<new_fish[1]:
                        new_pond.pop(len(new_pond)-1)
            else:
                new_pond+=[new_fish,]
    return len(new_pond)
