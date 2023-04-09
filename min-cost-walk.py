def path(prev, s, t):
    p = []
    dest = s
    while dest != t:
        p += [dest]
        dest = min([j for i,j in prev.items() if i == dest])
    return p

def min_cost_walk(WList, s, e, t):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys()
                           for (v,d) in WList[u]])
    (visited,distance) = ({},{})
    for v in WList.keys():
        (visited[v],distance[v]) = (False,infinity)
        
    distance[t] = 0
    prev = {}
    for u in WList.keys():
        nextd = min([distance[v] for v in WList.keys()
                        if not visited[v]])
        nextvlist = [v for v in WList.keys()
                        if (not visited[v]) and
                            distance[v] == nextd]

        if visited[s] and visited[e]:
            break
            
        nextv = min(nextvlist)
        visited[nextv] = True        
        for (v,d) in WList[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v],distance[nextv]+d)
                if distance[v] == distance [nextv] + d:
                    prev[v] = nextv
    
    return(distance[s] + distance [e], path(prev, s, t) +[t]+ path(prev,e,t)[::-1])
