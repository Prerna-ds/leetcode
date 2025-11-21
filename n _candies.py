def min_money(candy , k , n ):
    candy=sorted(candy)
    mini=0
    buy=0
    free=n-1
    while(buy<=free):
        mini+=candy[buy]
        buy+=1
        free=free-k
    return mini
def max_money(candy , k , n):
    maxi=0
    buy=n-1
    free=0
    candy=sorted(candy)
    while(free<=buy):
        maxi+=candy[buy]
        buy-=1
        free+=k
    return maxi


    
candy=[ 3,2, 1, 4]
k=2
n=4
ans=min_money(candy , k , n)
ans2=max_money(candy , k , n)
print(ans2)
print(ans)