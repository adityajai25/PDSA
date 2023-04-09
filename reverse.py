def reverse(root):
    if root.value==None or root.next==None:
        return root
    newroot=reverse(root.next)
    root.next.next=root
    root.next=None
    
    return newroot
