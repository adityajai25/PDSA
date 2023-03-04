def maxLessThan(root, k):
    if root.value == k:
        return root.value
    if root.isleaf():
        if root.value < k:
            return root.value
        else:
            return None
            
    if root.value > k:
        if root.left.isempty():
            return None
        return maxLessThan(root.left, k)
    else:
        if root.right.isempty():
            return root.value
        if root.right.value > k:
            return root.value
        return maxLessThan(root.right, k)
