"""
Dylan Davis
EECS 330 Lab 3
lab 03
9/11/2023
"""
class SLList:
    class IntNode:
        def __init__(self, item, next_node):
            self.item = item # int
            self.next = next_node # IntNode
            
    def __init__(self):
        self.first = None # initialize an empty list

    def addFirst(self, item):
        self.first = self.IntNode(item, self.first)

    def insert (self, item, position):
        node = self.IntNode (item, None)
        if self.first is None:
            self.addFirst(item)
        else:
            pointer = self.first
            count = 1
            while pointer.next is not None and count < position:
                pointer = pointer.next
                count = count + 1

            node.next = pointer.next
            pointer.next = node
        return self.first

    def reverse(self):  # previous = p current = c
        p = None
        c = self.first
        while c is not None:
            next_node = c.next
            c.next = p
            p = c 
            c = next_node
        self.first = p 

    def replicate(self):
        list = SLList()
        pointer = self.first

        while pointer is not None:
            for i in range (pointer.item):
                list.addFirst(pointer.item)
            pointer = pointer.next
        list.reverse()
        return list

    def equals(self, anotherList):
        p1 = self.first
        p2 = anotherList.first
        while p1 is not None and p2 is not None:
            if p1.item != p2.item:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return p1 is None and p2 is None

    def printList(self):
        p = self.first
        while p is not None:
            print(p.item, end = " ")
            p = p.next 
        print()


    
L = SLList()
L.addFirst(15)
L.addFirst(10)
L.addFirst(1)
print('List: ')
L.printList()

L.insert(5,1)
print("Inserting at specific position: (5, 1)")
L.printList() 

L.insert(20, 9)
print("Inserting at position greater than the list: (20, 9)")
L.printList()

print("Reversed list:") 
L.reverse()
L.printList()

dupe = L.replicate() 
print("Replicated List:")
dupe.printList()

LPrime = SLList() 
LPrime.addFirst(9)
LPrime.addFirst(6)
LPrime.addFirst(4)


LDp = SLList()
LDp.addFirst(9)
LDp.addFirst(6)
LDp.addFirst(4)

print ('L prime:')
LPrime.printList()
print ('L double prime:') 
LDp.printList()
if LPrime.equals(LDp): 
    print("The 2 Lists are equal")
else:
    print("The two Lists are not equal")

    
