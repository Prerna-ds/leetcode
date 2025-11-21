def rope_cost(n , cost):
    cst=0
    
    while(len(cost)>1):
        # cost.sort()
        n=sorted(cost)
        first=n[0]
        sec=n[1]
        n.pop(0)
        n.pop(0)
        c=first+sec
        cst+=c
        n.append(c)

    return cst


cost=[4 , 3 , 2 , 6]
n=4
ans=rope_cost(n , cost)
print(ans)