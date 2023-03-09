def mergeAndCount(A,B):
    m, n = len(A), len(B)
    C, i, j, k, count = [], 0, 0, 0, 0
    while k < m+n:
        if i == m:
            C.append(B[j])
            j, k = j+1, k+1
        elif j == n:
            C.append(A[i])
            i, k = i+1, k+1
        elif A[i] < B[j]:
            C.append(A[i])
            i, k = i+1, k+1
        else:
            C.append(B[j])
            j, k, count = j+1, k+1, count+(m-i)
    return C, count

def sortAndCount(A):
    n = len(A)

    if n <= 1:
        return A, 0

    L, countL = sortAndCount(A[:n//2])
    R, countR = sortAndCount(A[n//2:])

    B, countB = mergeAndCount(L, R)

    return B, countL+countR+countB

def countIntersection(x1, x2):
    z = list(zip(x1, x2))
    z.sort()
    A = [i[1] for i in z]
    L, ans = sortAndCount(A)
    return ans

