from math import sqrt

def isPrime(n):
    if(n<=1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if isPrime(i):
        c+=1
print(c)
