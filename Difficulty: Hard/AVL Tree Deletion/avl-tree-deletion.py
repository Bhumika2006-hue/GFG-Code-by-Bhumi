def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rotateRight(y):
    x = y.left
    T2 = x.right
    # Perform rotation
    x.right = y
    y.left = T2
    # Update heights
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x

def rotateLeft(x):
    y = x.right
    T2 = y.left
    # Perform rotation
    y.left = x
    x.right = T2
    # Update heights
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def deleteNode(root, key):
    # 1. Perform standard BST delete
    if not root:
        return root
    
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        # Node found - Case with one child or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # Case with two children: Get inorder successor
        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    if not root:
        return root

    # 2. Update height of current node
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    # 3. Get balance factor and rebalance
    balance = getBalance(root)

    # Left Heavy
    if balance > 1:
        if getBalance(root.left) >= 0: # Left Left Case
            return rotateRight(root)
        else: # Left Right Case
            root.left = rotateLeft(root.left)
            return rotateRight(root)

    # Right Heavy
    if balance < -1:
        if getBalance(root.right) <= 0: # Right Right Case
            return rotateLeft(root)
        else: # Right Left Case
            root.right = rotateRight(root.right)
            return rotateLeft(root)

    return root