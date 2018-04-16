from BinarySearchTreeDS.Node import Node

class BST:

    def __init__(self):
        self.rootNode = None

    def insert(self,data):
        if not self.rootNode:
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data)

    def remove(self, dataToremove):
        if self.rootNode:
            if self.rootNode.data == dataToremove:
                tempNode = Node(None)
                tempNode.leftChild = self.rootNode
                self.rootNode.remove(dataToremove,tempNode)
            else:
                self.rootNode.remove(dataToremove,None)

    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()

    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()

    def traverseInorder(self):
        if self.rootNode:
            self.rootNode.traverseInorder();