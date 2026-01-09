class Solution:
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        
        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y

    def insertToAVL(self, node, key):
        # 1. Perform standard BST insertion
        if not node:
            return Node(key)
        
        if key < node.data:
            node.left = self.insertToAVL(node.left, key)
        elif key > node.data:
            node.right = self.insertToAVL(node.right, key)
        else:
            return node # Duplicate keys not allowed in AVL
            
        # 2. Update height of this ancestor node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        
        # 3. Get the balance factor
        balance = self.getBalance(node)
        
        # 4. If unbalanced, handle the 4 cases
        
        # Left Left Case
        if balance > 1 and key < node.left.data:
            return self.rightRotate(node)
            
        # Right Right Case
        if balance < -1 and key > node.right.data:
            return self.leftRotate(node)
            
        # Left Right Case
        if balance > 1 and key > node.left.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
            
        # Right Left Case
        if balance < -1 and key < node.right.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
            
        return node