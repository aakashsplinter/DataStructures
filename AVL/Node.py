
class Node(object):

    def __init__(self, data,parentNode):
        self.data = data
        self.parentNode = parentNode
        self.rightchild = None
        self.leftchild = None
        self.balance = 0

    def insert(self,data,parentNode):

        if(data < self.data):
            if not self.leftchild:
                self.leftchild = Node(data,parentNode)
            else:
                self.leftchild.insert(data,parentNode)
        else:
            if not self.rightchild:
                self.rightchild = Node(data, parentNode)
            else:
                self.rightchild.insert(data, parentNode)

        return parentNode


    def traverseInOrder(self):
        if self.leftchild:
            self.leftchild.traverseInOrder()

        print(self.data)

        if self.rightchild:
            self.rightchild.traverseInOrder()


    def getMax(self):
        if not self.rightchild:
            return self.data
        else:
            return self.rightchild.getMax()

    def getMin(self):
        if not self.leftchild:
            return self.data
        else:
            return self.leftchild.getMin()