from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    # Add element to stack
    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    # Remove the top element of stack
    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empty!")
    
    def peek(self):
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty!")

    # Length of stack
    def __len__(self):
        return self._size
    
    # Shows stack content
    def __repr__(self):
        r=""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    list = Stack()
    list.append(19)
    list.append(112)
    list.append(65)
    list.append(111)
    list.append(559)