N = int(input('N = '))
k1=0
k2=0
k3=0
for i in range(N):
    a = int(input())
    if a==0:
      k1=k1+1
    elif a>0:
      k2=k2+1
    else:
      k3=k3+1
print(k1)
print(k2)
print(k3)
