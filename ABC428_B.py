from collections import Counter

n,k=map(int,input().split())
s=list(input())

_strings=[s[i:i+k] for i in range(n-k+1)]

strings=["".join(word) for word in _strings]

count=Counter(strings)
max_count=count.most_common(1)[0][1]
result=sorted([str for str,cnt in count.items() if cnt==max_count])

print(max_count)
print(*result)