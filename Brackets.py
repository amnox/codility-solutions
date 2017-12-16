
def solution(S):
    open_b = ['[','{','(']
    close_b = [']','}',')']
    tray = []
    for bracket in S:
        if bracket in open_b:
            tray= tray + [bracket,]
        elif bracket in close_b:
            if len(tray)==0:
                return 0
            if close_b.index(bracket)==open_b.index(tray[-1]):
                tray.pop(len(tray)-1)
            else: return 0
    if len(tray)!=0:
        return 0
    return 1

