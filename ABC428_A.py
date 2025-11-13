# s,a,b,x=map(int,input().split())

# count=int(x/(a+b))
# extra=x%(a+b)
# if extra>a:
#   print(s*a*(count+1))
# else:
#   print(count*s*a+extra*s)

s, a, b, x = map(int, input().split())

count, extra = divmod(x, a + b)
print(s * (a * count + min(a, extra)))
