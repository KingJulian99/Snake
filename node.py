class node:
    def __init__(self, x_coord, y_coord, head=False, trailing_node=False):
        self.x = x_coord
        self.y = y_coord
        self.head = head
        self.nextNode = None
        self.prevNode = None
        self.trailing_node = trailing_node

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def setPrev(self, prevNode):
        self.prevNode = prevNode

    def getNext(self):
        return self.nextNode

    def getPrev(self):
        return self.prevNode

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y
    
    def setY(self, y):
        self.y = y

    def isTrailing(self):
        return self.trailing_node