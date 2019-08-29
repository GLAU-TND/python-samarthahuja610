n=int(input())
radius=input().split()
for i in range(n):
    radius[i]=int(radius[i])
a=[]

for i in range(n):
    b=radius.count(radius[i])
    a.append(b)
print(max(a))
