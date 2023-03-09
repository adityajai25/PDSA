def Brute_ClosestPair(P):
    dists = []
    for i in P:
        for j in P:
            if i != j:
                x1, y1 = i
                x2, y2 = j
                d = ((x2-x1)**2 + (y2-y1)**2)**0.5
                dists.append((i, j, d))
    dists.sort(key=lambda x: x[2])
    return dists[0]

def ClosestPair(Px, Py):
    if len(Px) <= 3:
        return Brute_ClosestPair(Px)
    
    Qx, Rx = Px[:len(Px)//2], Px[len(Px)//2:]
    Qy, Ry = [], []
    xR = min(Rx)[0]
    for i in Py:
        if i[0] < xR:
            Qy.append(i)
        else:
            Ry.append(i)
    
    q1, q2, dQ = ClosestPair(Qx, Qy)
    r1, r2, dR = ClosestPair(Rx, Ry)

    delta = min(dQ, dR)
    Sy = []
    for i in Qy:
        if xR - i[0] <= delta:
            Sy.append(i)
    for j in Ry:
        if j[0] - xR <= delta:
            Sy.append(j)
    Sy.sort()
    dS = delta

    S = []
    c = 1
    for s1 in Sy:
        if c < len(Sy):
            for s2 in Sy[c:c+16]:
                x1, y1 = s1
                x2, y2 = s2
                d = ((x2-x1)**2 + (y2-y1)**2)**0.5
                if d < delta:
                    dS = d
                    S.append((s1, s2, dS))
        c += 1

    if S != []:
        S.sort()
        return S[0]
    else:
        final = [(q1, q2, dQ), (r1, r2, dR)]
        final.sort(key=lambda x: x[2])
        return final[0]

def minDistance(Points):
    Px = sorted(Points)
    Py = sorted(Points, key=lambda x: x[1])

    closest_pair_and_distance = ClosestPair(Px, Py)
    return round(closest_pair_and_distance[2], 2)
