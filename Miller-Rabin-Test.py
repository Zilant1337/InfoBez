# from GCD import GCD
import math
import random

def MLT(n,k):
    if(n<=2):
        print("N is a prime number")
        return True
    if(n%2==0):
        print("N is a composite number")
        return False
    s=1
    d=(n-1)/2
    print("s= ",s," d= ",d, " n-1= ",n-1," 2^s*d= ",math.pow(2,s)*d)
    while(d%2==0):
        d/=2
        s+=1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(int(a), int(d), int(n))
        if x == 1 or x == n - 1:
            continue
        for _ in range(s-1):
            x = pow(int(x), int(2), int(n))
            if x == n - 1:
                break
        else:
            return False
    return True

n= int(input())
k= int(input())
print(MLT(n,k))
