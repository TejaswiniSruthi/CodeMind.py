n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in arr:
    if((i<a or i>b)):
        c.append(i)
if (len(c)==0):
    print(-1)
else:
    print(min(c))
