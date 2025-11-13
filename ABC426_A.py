x,y=map(str,input().split())

order={"Ocelot":1,"Serval":2,"Lynx":3}

if(order[x]>=order[y]):
  print("Yes")
else:
  print("No")