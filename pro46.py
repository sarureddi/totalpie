u1=int(input())
v1=list(map(int,input().split()))
a1=0
b1=0
v1.sort(reverse=True)
for i1 in v1:
  v1=a1+i1
  if b1>v1:
    a1=v1
  else:
    a1=b1
    b1=v1
print(a1,b1)
