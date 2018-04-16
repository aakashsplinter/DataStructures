from AVL.Node import Node

class BalancedTree(object):

    def __init__(self):
        self.rootNode = None

    def insert(self,data):
        parentNode = self.rootNode
        if self.rootNode == None:
            parentNode = Node(data,None)
            self.rootNode = parentNode
        else:
            parentNode = self.rootNode.insert(data, self.rootNode)

        self.rebalanceTree(parentNode)

    def rebalanceTree(self,parentNode):
        self.setbalance(parentNode)

    def height(self, node):
        if node == None:
            return -1
        else:
            return 1+max(self.height(node.leftchild),self.height(node.rightchild))

    def setbalance(self,node):
        node.balance = (self.height(node.rightchild) - self.height(node.leftchild))

    def rebalance(self,parentNode):
        self.setbalance(parentNode)
        if parentNode.balance < -1:
            if self.height(parentNode.leftchild.leftchild) >= self.height(parentnode.leftchild.rightchild):
                parentNode = self.rotateRight(parentNode)
            else:
                parentNode = self.rotateLeftRight(parentNode)
        elif parentNode.balance > 1:
            if self.height(parentNode.rightchild.rightchild) >= self.height(parentNode.rightchild.leftchild):
                parentNode = self.rotateLeft(parentNode)
            else:
                parentNode = self.rotateRightLeft(parentNode)

        if parentNode.parentNode is not None:
            self.rebalanceTree(parentNode.parentNode)
        else:
            self.rootNode = parentNode;

    def rotateLeftRight(self,node):
        print(" Rotate Left Right ..")
        node.leftchild = self.rotateRight(node.leftchild)
        return self.rotateRight(node)

    def rotateRightLeft(self, node):
        print(" Rotate Right Left....")
        node.rightchild = self.rotateLeft(node.rightchild)
        return self.rotateLeft(node)

    def rotateLeft(self,node):
        print(" Rotate Left ..")
        b = node.rightchild
        b.parentNode = node.parentNode
        node.rightchild = b.leftchild
        if node.rightchild is not None:
            node.rightchild.parentNode = node

        b.leftchild = node
        node.parentNode = b;

        if b.parentNode is not None:
            if b.parentNode.rightchild == node:
                b.parentNode.rightchild = b
            else:
                b.parentNode.leftchild = b

        self.setbalance(node)
        self.setbalance(b)

        return b;

    def rotateRight(self,node):
        print("Rotate right .. ")
        b = node.leftchild
        b.parentNode = node.parentNode
        node.leftchild = b.rightchild
        if node.leftchild is not None:
            node.leftchild.paentNode = node

        b.rightchild = Node
        node.parentNode = b
        if b.parentNode is not None:
            if b.parentNode.rightchild == node:
                b.parentNode.rightchild = b
            else:
                b.parentNode.leftchild = b

        self.setbalance(node)
        self.setbalance(b)
        return b

    def traverseInOrder(self):
        self.rootNode.traverseInOrder()