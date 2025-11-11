# import collections

# def Permu(a, b):
#     num = 1
#     for i in range(a, a - b, -1):
#         num *= i
#     return num
# def Conbi(a,b):
#   return Permu(a,b)/Permu(b,1)

# N=map(int,input().split())
# A=list(map(int,input().split()))

# B=collections.Counter(A)
# indicates=set(A)
# count=0

# for i in indicates:
#   if(B[i]>1):
#     count+=(len(A)-B[i])*Conbi(B[i],2)

# print(int(count))

from collections import Counter
from math import comb

n = int(input())
A = list(map(int, input().split()))
B = Counter(A)

ans = sum(cnt * (cnt - 1) * (n - cnt) // 2 for cnt in B.values())
print(ans)
