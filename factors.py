n=int(input("enter a number:"))
i=1
s=0
while i!=n:
  if n%i==0:
    print(i)
    s+=i
  i+=1
  print("Sum of factors is:,s")
  if s==n:
    print("perfect number")
  else:
    print("not a perfect number")
