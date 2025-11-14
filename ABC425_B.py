n = int(input())
a = list(map(int, input().split()))

# 非 -1 値の重複チェック（-1 は無視）
used = set()
count_nonneg = 0
for x in a:
    if x != -1:
        count_nonneg += 1
        if x in used:
            print("No")
            exit()
        used.add(x)

# 使われていない数字を列挙
unused = [i for i in range(1, n+1) if i not in used]

# -1 の箇所に unused を順に入れていく（任意に入れてよい）
res = []
it = iter(unused)
for x in a:
    if x == -1:
        res.append(next(it))
    else:
        res.append(x)

print("Yes")
print(*res)
