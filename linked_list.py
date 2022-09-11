class linked_list:
    def __init__(self, head_node):
        self.head = head_node

    def getHead(self):
        return self.head

    def getTail(self):
        node = self.head

        while(node.nextNode != None):
            node = node.nextNode

        return node