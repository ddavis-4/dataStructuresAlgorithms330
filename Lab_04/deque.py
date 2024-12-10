"""
Dylan Davis |3047302
EECS 330 lab 04
9/23/2023
"""


class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def empty(self):
        if self.size == 0: return True

    def get_size(self) -> int:
        return self.size

    def push_front(self, data):
        # case 1: if is empty
        if self.empty:
            self.front = Node(data)
            self.front = self.back
            # case 2: if is not empty
        else:
            self.front.next = Node(data)
            self.front.next.prev = self.front
            self.front = self.front.next
        self.size += 1

    def push(self, data):
        # case 1: is empty
        n = Node(data)
        if self.empty():
            self.front = n
            self.back = n
        # case 2: is not empty
        else:
            n.prev = self.back
            self.back.next = n
            self.back = n
        self.size += 1

    def pop_front(self) -> int:
        if self.empty():
            raise Exception("Deque is empty")
        I = self.front.item
        self.front = self.front.prev
        self.front.next = None
        self.size -= 1

        return I

    def pop(self) -> int:
        if self.empty():
            raise Exception("Deque is empty")
        I = self.back.item
        self.back = self.back.prev
        self.back.next = None
        self.size -= 1

        return I

    def get_front(self) -> int:
        if self.empty():
            raise Exception("Deque is empty")
        else:
            return self.front.item

    def get_back(self) -> int:
        if self.empty():
            raise Exception("Deque is empty")
        else:
            return self.back.item

if __name__ == '__main__':
    pass


