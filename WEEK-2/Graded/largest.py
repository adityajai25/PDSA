def findLargest(L):
  left = 0
  s = len(L)
  right = s-1  
  if (s==1):
    return L[0]
  while (left<=right):
    mid=(left+right)//2
    if (mid == s-1):
      nextToMid = 0
    else:
      nextToMid = mid+1
    if (L[mid] > L[nextToMid]):
      return L[mid]
    elif (L[mid] < L[0]):
      right = mid-1
    else:
      left = mid+1
