import heapq
def pq(cost):
    heapq.heapify(cost)
    tot=0

    while(len(cost)>1):
        first=heapq.heappop(cost)
        sec=heapq.heappop(cost)
        merge=first+sec
        tot+=merge
        heapq.heappush(cost , merge)
    return tot


    
cost=[4 , 3 , 2 , 6]
n=4
ans=pq(cost)
print(ans)