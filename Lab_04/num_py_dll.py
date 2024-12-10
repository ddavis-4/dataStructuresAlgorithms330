import numpy as np

class Deque:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        # Initialize front and rear pointers.
        self.front = -1
        self.back = -1
        # Initialize size of the deque.
        self.size = 0
        # Use a zero initialized NumPy array to store elements.
        self.array = np.zeros(self.capacity, dtype=object)

    def empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def push_front(self, data):
        if self.empty():
            self.array[0] = data
            self.front = 0
            self.back = 0
        elif self.get_size() < self.capacity:
            self.array[1:] = self.array[:-1]  
            self.array[0] = data
            self.back += 1
        else:
            self.resize()
            self.array[1:] = self.array[:-1]  
            self.array[0] = data
            self.back += 1

    def push(self, data):
        if self.empty():
            self.array[0] = data
            self.front = 0
            self.back = 0
        elif self.get_size() < self.capacity:
            self.array[self.back + 1] = data
            self.back += 1
        else:
            self.resize()
            self.array[self.back + 1] = data
            self.back += 1

    def pop_front(self):

        if self.empty():
            return None
        data = self.array[self.front]
        if self.front == self.back:
            self.front = self.back = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data

    def pop(self):

        if self.empty():
            return None
        data = self.array[self.back]
        if self.front == self.back:
            self.front = self.back = -1
        else:
            self.back = (self.back - 1) % self.capacity
        self.size -= 1
        return data

    def resize(self):
        new_capacity = self.capacity * 2
        tmp = np.zeros(new_capacity, dtype=object)
        for i in range(self.size:
            tmp[i] = self.array[i]

        self.array = tmp
        self.capacity = new_capacity

def isPalindrome(s: str) -> bool:
    deque = Deque()

    s = s.replace(" ", "")

    for i in s:
        deque.push(i)

    while deque.get_size() > 1:
        if deque.pop_front() != deque.pop():
            return False
    return True
def reverse_deque(deque):
    reversed_deque = Deque()

    while not deque.empty():
        reversed_deque.push(deque.get_back())
        deque.pop()
    return reversed_deque

if __name__ == '__main__':

    deque = Deque()

    deque.push(1)
    deque.push(2)
    deque.push(3)

    reversed_deque = reverse_deque(deque)
    while not reversed_deque.empty():
        print(reversed_deque.pop_front())

test1 = "racecar"
test2 = "hello"
print(isPalindrome(test1))
print(isPalindrome(test2))