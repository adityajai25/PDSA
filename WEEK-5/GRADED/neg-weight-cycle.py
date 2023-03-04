def IsNegativeWeightCyclePresent(WList):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])
    distance = {}
    for v in WList.keys():
        distance[v] = infinity
        
    distance[0] = 0
    for i in range(len(WList.keys()) + 3):
        for u in WList.keys():
            for (v,d) in WList[u]:
                distance[v] = min(distance[v], distance[u] + d)
        
    for u in WList.keys():
        for (v,d) in WList[u]:
            if distance[v] > distance[u] + d:
                return True
    return False


size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    
print(IsNegativeWeightCyclePresent(WL))
