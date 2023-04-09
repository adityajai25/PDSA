def findMasterTank(tanks, pipes):
  
  indegree={}
  l=[]
  for i in tanks:
    indegree[i]=0

  for j in pipes:
    indegree[j[1]]+=1
 
  for i in tanks:
    if indegree[i]==0:
      l.append(i)
  if len(l)==1:
      return(l[0])

  return 0
