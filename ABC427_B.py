n=int(input())

def func(x):
  return sum(map(int, str(x)))

total=1
for i in range(n-1):
  total+=func(total)
print(total)