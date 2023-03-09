def MoM7(arr):
    if len(arr) <= 7:
        arr.sort()
        return arr[len(arr)//2]

    M = []
    for i in range(0, len(arr), 7):
        X = arr[i:i+7]
        X.sort()
        M.append(X[len(X)//2])

    return MoM7(M)

def MoM7Pos(arr):
    median = MoM7(arr)
    less_than_median_dict = {}
    for i in arr:
        if i < median:
            less_than_median_dict[i] = less_than_median_dict.get(i, 0) + 1
    return sum(less_than_median_dict.values())
