# O(N): Time complexity

def find(root, element):
    if root.data == element:
        return True
    
    isFound = False
    for child in root.children:
        if find(child, element):
            isFound = True
            break
    return isFound