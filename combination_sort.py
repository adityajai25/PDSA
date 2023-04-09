import string
def combinationSort(strList):
  groups = {k: [] for k in string.ascii_lowercase}  
  for i in range(len(strList)):
    char=strList[i][0]
    groups[char].append(strList[i])
  strList=[]
  for char in groups.keys():
    for s in groups[char]:
      strList.append(s)
  L1 = strList.copy() 
  i = 1
  left = 0
  while i<len(strList):
    right = i
    while(right>left and strList[right][0] == strList[right-1][0] and int(strList[right-1][1:])<int(strList[right][1:])):
      strList[right], strList[right-1] = strList[right-1], strList[right]
      right -= 1
    i += 1
  return L1, strList
