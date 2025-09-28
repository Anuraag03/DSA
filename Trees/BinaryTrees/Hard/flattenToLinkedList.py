def flatten(root):
    current = root
    while current:
        if current.left:
            temp = current.left
            while temp.right:
                temp = temp.right
            temp.right = current.right
            current.right = current.left
            current.left = None
        current = current.right