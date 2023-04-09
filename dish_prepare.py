def DishPrepareOrder(order_list):
  menu=[1001,1002,1003,1004,1005,1006,1007,1008,1009]
  dic={}
  for i in menu:
    dic[i]=order_list.count(i)

  return SortDishes(menu,dic)
  
def SortDishes(L,d):
  n = len(L)
  if n < 1:
      return(L)
  for i in range(n):
      j = i
      while(j > 0 and d[L[j]] > d[L[j-1]]):
        (L[j],L[j-1]) = (L[j-1],L[j])
        j = j-1
#to remove dishes that have 0 orders
  for i in d:
    if d[i]==0:
      L.remove(i)

  return L
