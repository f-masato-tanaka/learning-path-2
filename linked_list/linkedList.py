from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    # Add element to list
    def append(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size = self._size + 1
    
    # Length of list
    def __len__(self):
        return self._size
    
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        return pointer

    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("List index out of range")
        pass

    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List index out of range")
        pass
    
    # Search inside list
    def index(self, elem):
        pointer = self.head
        i = 0
        while (pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError(f"{elem} is not in list")
    
    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node = Node(elem)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1
    
    def remove(self, elem):
        if self.head == None:
            raise ValueError(f"{elem} is not in list")
    
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True
        raise ValueError(f"{elem} is not in list")

    def __repr__(self):
        r=""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    list = LinkedList()
    list.append(19)
    list.append(112)
    list.append(65)
    list.append(111)
    list.append(559)