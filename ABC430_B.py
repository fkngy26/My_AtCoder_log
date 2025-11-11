import copy

N,M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

result=[]

for y in range(N-M+1):
  for x in range(N-M+1):
    pad=[['*']*M for _ in range(M)]
    for i in range(M):
      for j in range(M):
        pad[i][j]=grid[y+i][x+j]

    flag=0
    for _pad in result:
      if pad==_pad:
        flag=1
        break
    if flag==0:
      result.append(copy.deepcopy(pad))
print(len(result))

# N, M = map(int, input().split())
# grid = [list(input()) for _ in range(N)]

# patterns = set()

# for y in range(N - M + 1):
#     for x in range(N - M + 1):
#         pattern = tuple(tuple(row[x:x+M]) for row in grid[y:y+M])
#         patterns.add(pattern)

# print(len(patterns))
