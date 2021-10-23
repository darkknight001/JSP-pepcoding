# Integer max and min are different in Java and Python

ceil = 2147483647
floor = -2147483648

def ceilFloor(root, data):
    global ceil, floor
    if root.data<data:
        floor = max(floor, root.data)
    elif root.data==data:
        pass
    else:
        ceil = min(ceil, root.data)
    
    
    for child in root.children:
        ceilFloor(child, data)
