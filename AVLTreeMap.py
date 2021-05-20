"""
    This program implement AVL Tree Map Data structure
    Data: March 4th, 2021
    Written By: Ngoc Bao Han, Nguyen
    Student ID: 20188794
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None
        self.parent = None
        self.height = 1

class AVLTreeMap:
    """
        This class implements AVL Tree Map and its functionality
        (1) get(self, key): find value given key, else return False
        (2) put(self, key, val): recursively add a new node into the tree
        (3) rebalance(self, node, path): checking whether node addition cause unbalance
        (4) getHeight(self, node): return node's height
        (5) shifting(self, a, b, c): consider 4 cases(LL, RR, LR, RL) to tailor rotation solutions
        (6) rightRotate(self, node)
        (7) leftRotate(self, node)
    """
    def __init__(self):
        self.root = None

    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.get_recur(self.root, key)

    def get_recur(self, node, key):
        if key < node.key:
            if node.left is None:
                return False
            return self.get_recur(node.left, key)
        elif key > node.key:
            if node.right is None:
                return False
            return self.get_recur(node.right, key)
        else:
            return node.val

    def put(self, key, val):
        if self.root is None:
            self.root = Node(key, val)
        else:
            self.put_recur(self.root, key, val)

    def put_recur(self, node, key, val):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, val)
                node.left.parent = node
                self.rebalance(node.left)
            else:
                self.put_recur(node.left , key, val)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, val)
                node.right.parent = node
                self.rebalance(node.right)
            else:
                self.put_recur(node.right, key, val)

    def rebalance(self, node, path = []):
        if node.parent is None:
            return
        path = [node] + path

        leftHeight = self.getHeight(node.parent.left)
        rightHeight = self.getHeight(node.parent.right)

        # case of unbalance detected
        if abs(leftHeight - rightHeight) > 1:
            path = [node.parent] + path
            self.shifting(path[0], path[1], path[2])
            return

        height = 1 + node.height
        if height > node.parent.height:
            node.parent.height = height

        self.rebalance(node.parent, path)

    def getHeight(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def shifting(self, a, b, c):
        # Left Left case
        if b == a.left and c == b.left:
            self.rightRotate(a)
        # Left Right case
        elif b==a.left and c==b.right:
            self.leftRotate(b)
            self.rightRotate(a)
        # Right Right case
        elif b == a.right and c == b.right:
            self.leftRotate(a)
        # Right Left case
        elif b==a.right and c == b.left:
            self.rightRotate(b)
            self.leftRotate(a)

    def rightRotate(self, node):
        # hold parent node to move around left and right child
        tempRoot = node.parent
        block = node.left # this node will become the center node
        # hold grandchild node to transfer to left of current
        tempNode = block.right
        block.right = node

        node.parent = block
        node.left = tempNode

        if tempNode is not None:
            tempNode.parent = node
        block.parent = tempRoot # reassigning parent relationship

        if block.parent is None: # if the rearrangement is happening at root node
            self.root = block
        else:
            if block.parent.left == node:
                block.parent.left = block
            else:
                block.parent.right = block
        # updating height for two new left and right node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        block.height = 1 + max(self.getHeight(block.left), self.getHeight(block.right))

    def leftRotate(self, node):
        tempRoot = node.parent
        block = node.right
        tempNode = block.left
        block.left = node

        node.parent = block
        node.right = tempNode

        if tempNode is not None:
            tempNode.parent = node
        block.parent = tempRoot
        if block.parent is None:
            self.root = block
        else:
            if block.parent.left == node:
                block.parent.left = block
            else:
                block.parent.right = block

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        block.height = 1 + max(self.getHeight(block.left), self.getHeight(block.right))

if __name__ == "__main__":
    testing_dict = {
        15: "bob",
        20: "anna",
        24: "tom",
        10: "david",
        13: "david",
        7: "ben",
        30: "karen",
        36: "erin",
        25: "david"
    }

    tree = AVLTreeMap()
    for key, val in testing_dict.items():
        tree.put(key, val)

    print(tree.get(24)) # testing to get 'tom'

