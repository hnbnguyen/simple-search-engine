"""
    This program implements Binary Search Tree with additional functionality
    Date: March 4th, 2021
    Written by: Ngoc Bao Han, Nguyen
    Student ID: 20188974
"""
class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.value = val
        self.height = 1;

class BinarySearchTree:
    """
    This class defines BST functions as well as additional functionality specified by assignment
    (1) getRoot(self): return the current root node
    (2) insert(self, val): call a recursive function to add a new value to search tree
    (3) printTree(self): Print out the tree in ascending order
    (4) TestingUpdateAll(self): recursively update all heights in the tree
    (5) updateHeight(self, node): update the height of current node
    (6) getTotalHeight(self): get sum of all heights of nodes in tree with O(n) time complexity
    (7) getWeightBalanceFactor(self): measure how well balanced the tree is
    """
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root;

    def insert(self, val):
        # inserting new value into the tree, if the tree is already created, jump into insert_recur
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_recur(self.root, val)

    def insert_recur(self, node, val):
        # recursively find a new place to add the new value
        if val < node.value:
            if node.left is None:
                node.left = Node(val)
                self.testingUpdateAll()
            else:
                self.insert_recur(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
                self.testingUpdateAll()
            else:
                self.insert_recur(node.right, val)

    def printTree(self):
        # printing the binary tree in ascending order, if tree exists, go into print_recur
        if self.root is not None:
            self.printTree_recur(self.root)

    def printTree_recur(self, node):
        if node is not None:
            self.printTree_recur(node.left)
            print(str(node.value) + " ")
            self.printTree_recur(node.right)

    def testingUpdateAll(self):
        if self.root is not None:
            self.testingUpdateIndNode(self.root)

    def testingUpdateIndNode(self, node):
        if node is not None:
            self.testingUpdateIndNode(node.left)
            node.height = self.updateHeight(node)
            self.testingUpdateIndNode(node.right)

    def updateHeight(self, node):
        if node is None:
            return -1
        else:
            return max(self.updateHeight(node.left), self.updateHeight(node.right)) + 1

    def getTotalHeight(self):
        if self.root is not None:
            return self.sum_nodes(self.root)

    def addAllTreeHeight(self, node, count):
        if node is not None:
            self.addAllTreeHeight(node.left, count)
            count += node.height
            self.addAllTreeHeight(node.right, count)
        return count

    def sum_nodes(self, node):
        if node is None:
            return 0
        return node.height + self.sum_nodes(node.left) + self.sum_nodes(node.right)

    def getWeightBalanceFactor(self):
        self.allWeightFactor = []
        if self.root is None:
            return None
        self.findBalanceFactor(self.root)
        return max(self.allWeightFactor)

    def findBalanceFactor(self, node):
        if node is None:
            return 0
        weightDif = abs(self.findBalanceFactor(node.left)) - abs(self.findBalanceFactor(node.right))
        self.allWeightFactor.append(weightDif)
        return self.findBalanceFactor(node.left) + self.findBalanceFactor(node.right) + 1

    def print2DUtil(self,root, space):

        # Base case
        if (root == None):
            return

        # Increase distance between levels
        space += 10

        # Process right child first
        self.print2DUtil(root.right, space)

        # Print current node after space
        # count
        print()
        for i in range(10, space):
            print(end=" ")
        print(root.value)

        # Process left child
        self.print2DUtil(root.left, space)

        # Wrapper over print2DUtil()

    def print2D(self):

        # space=[0]
        # Pass initial space count as 0
        self.print2DUtil(self.root, 0)

if __name__ == "__main__":
    b = BinarySearchTree()
    a = [6,4,8,9,7,5,3]
    for item in a:
        b.insert(item)
    b.print2D()
    print("____")
    print("Weight Balance Factor: ", b.getWeightBalanceFactor())
    print("Total Height of tree: ",b.getTotalHeight())


