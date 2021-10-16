def nodeToRootPath(root, element):
    psf = []
    if root.data == element:
        psf.append(root.data)
        return psf
    
    isFound = False
    for child in root.children:
        psf = nodeToRootPath(child, element)
        if len(psf)>0:
            psf.append(root.data)
            break
    return psf

def lca(root, e1, e2):
    p1 = nodeToRootPath(root, e1)
    p2 = nodeToRootPath(root, e2)
    # print(p1, p2)
    i = len(p1)-1;
    j = len(p2)-1;
    
    while(i>=0 and j>=0 and p1[i]==p2[j]):
        i-=1
        j-=1
    # print(i," ",j)
    return p1[i+1]