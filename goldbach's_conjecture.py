def prime(n):
  if n < 2:
    return False
  for i in range(2,n//2+1):
    if n%i==0:
      return False
  return True

def Goldbach(n):
  Res=[]
  for i in range((n//2)+1):
    if prime(i)==True:
      if prime(n-i)==True:
        Res.append((i,n-i))
  return(Res)
n=int(input())
print(sorted(Goldbach(n)))
