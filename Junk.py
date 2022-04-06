n=int(input())
a=[]
def f(k,n):
    if n%2==0 and k%2==0 or n%2!=0 and k%2!=0:
        x=1;y=2;z=3;o=0
    if n%2!=0 and k%2==0 or n%2==0 and k%2!=0:
        x=1;y=3;z=2;o=0
    for i in range(2**k-1,2**n-1,2**(k+1)):
        a[i].append(k+1)
        a[i].append(x)
        a[i].append(y)
        o=x;x=y;y=z;z=o
for i in range(2**n-1):
    a.append([])
for i in range(n):
    f(i,n)
for i in range(len(a)):
    print(a[i][0],a[i][1],a[i][2])