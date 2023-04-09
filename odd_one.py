def odd_one(L):
  P = {}
  for elem in L:
    if type(elem) not in P:
      P[type(elem)] = 0
    P[type(elem)] += 1
  for key, value in P.items():
    if value == 1:
      return key.__name__

print(odd_one(eval(input().strip())))
