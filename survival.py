def survival(n , m , s):
    if(m>n):
        return -1
    sunday=s//7
    buy_days=s-sunday
    # on 7th 14 ... we cant buy the food
    food_required=s*m
    if food_required%n==0:
        ans=food_required//n
    else:
        ans=food_required//n +1

    if(ans<=buy_days):
        return ans
    else:
        return -1
    
n=16
m=2
s=10
ans=survival(n , m,s)
print(ans)