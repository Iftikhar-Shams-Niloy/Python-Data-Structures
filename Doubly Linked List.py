class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p

class DoublyList:
    def __init__(self, array):
        self.head = Node(None, None, None)
        tail = self.head
        for i in range(len(array)):
            n = Node(array[i], None, None)
            tail.next = n
            n.prev = tail
            tail = tail.next
        tail.next = self.head
        self.head.prev = tail

    def countNode(self):
        count = 0
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count

    def forwardPrint(self):
        pointer = self.head.next
        while pointer != self.head:
            if pointer != self.head.prev:
                print(pointer.element, end=", ")
            else:
                print(pointer.element)
            pointer = pointer.next

    def backwardPrint(self):
        pointer = self.head.prev
        while pointer != self.head:
            if pointer != self.head.next:
                print(pointer.element, end=", ")
            else:
                print(pointer.element)
            pointer = pointer.prev

    def insert(self, elem, idx):
        head = self.head
        tail = head.next

        if idx >= self.countNode() + 1 or idx < 0:
            return None

        myNewNode = Node(elem, None, None)

        loop_counter = 0
        while tail != head:
            if loop_counter == idx:

                pred = tail.prev

                myNewNode.next = tail
                myNewNode.prev = pred

                pred.next = myNewNode
                tail.prev = myNewNode

            tail = tail.next
            loop_counter += 1

print()
##########
# >>> Task-5 <<<
print(">>> Task-5<<<")
my_arr = [10,34,12,4,-99,100]
myDoublyLL = DoublyList(my_arr)
print(myDoublyLL.head.prev.element)
myDoublyLL.forwardPrint()
myDoublyLL.backwardPrint()