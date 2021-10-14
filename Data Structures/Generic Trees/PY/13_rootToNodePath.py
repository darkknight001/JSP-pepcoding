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