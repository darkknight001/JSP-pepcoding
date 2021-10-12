def mirror(root):
    root.children.reverse()

    for child in root.children:
        mirror(child)
    