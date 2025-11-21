class meeting:
    def __init__(self,starttime , endtime , pos):
        self.starttime=starttime
        self.endtime=endtime
        self.pos=pos

        

def meet(start , end , n):
    meets=[meeting(start[i] , end[i] , i+1)for i in range (n)]
    meets.sort(key=lambda m: m.endtime)
    free_time=-1
    res=[]
    for i in range(n):
        if meets[i].starttime>free_time:
            free_time=meets[i].endtime
            res.append(meets[i].pos)
    res.sort()
    return res

    
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
ans=meet(start , end , 6)
print(ans)
