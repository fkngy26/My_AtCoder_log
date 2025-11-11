N,M=map(int,input().split())
A=list(map(int,input().split()))

sum=0
for i in range(N):
  sum+=A[i]

flag=False
for i in range(N):
  if M==sum-A[i]:
    flag=True
if flag:
  print("Yes")
else:
  print("No")