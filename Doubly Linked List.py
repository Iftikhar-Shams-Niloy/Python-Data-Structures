class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p

class DoublyList:
    def __init__(self, array): # array = [11, 22, 33]
        self.head = Node(None, None, None)
        tail = self.head
        for i in range(len(array)):
            new = Node(array[i], None, None)
            tail.next = new
            new.prev = tail
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

    def nodeAt(self, index):
        total_nodes = self.countNode()
        head = self.head
        temp = head.next
        # CHECKING IF THE GIVEN 'index' IS VALID OR NOT!
        if index >= total_nodes or index < 0:
            print("Index Out of Range!!!")

        if index == total_nodes:
            return head.prev
        elif index == 0:
            return temp
        else:
            loop_counter = 0
            while temp != head:
                if loop_counter == index:
                    return temp
                temp = temp.next
                loop_counter += 1

    def insert(self, elem, index):
        head = self.head
        tail = head.next
        if index >= self.countNode() + 1 or index < 0:
            print("Index Out of Range!!!")

        my_new_node = Node(elem, None, None)  # Creating a new "Node" class

        loop_counter = 0
        while tail != head:
            if loop_counter == index:
                temp = tail.prev
                my_new_node.next = tail
                my_new_node.prev = temp
                temp.next = my_new_node
                tail.prev = my_new_node
            tail = tail.next
            loop_counter += 1

    def remove(self, index):
        head = self.head
        temp = head.next
        total_nodes = self.countNode()
        if index >= total_nodes or index < 0:
            print("Index Out of Range!!!")

        loop_counter = 0
        while temp != head:
            # The code lines inside if will only run Once when it finds the right NODE to remove
            if loop_counter == index:
                previus_node = temp.prev
                next_node = temp.next
                previus_node.next = next_node
                next_node.prev = previus_node
                removed = temp.element
                temp.prev = None
                temp.next = None
                return str(removed)

            temp = temp.next
            loop_counter += 1


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




print("####################################################")
my_arr = [10,34,12,4,-99,100]
myDoublyLL = DoublyList(my_arr)
print(myDoublyLL.head.prev.element)
print("#####################################################")
myDoublyLL.forwardPrint()
myDoublyLL.backwardPrint()
print("#####################################################")
myDoublyLL.insert(999999,3)
myDoublyLL.forwardPrint()
print("#####################################################")
myNode = myDoublyLL.nodeAt(3)
print(myNode.element)
print("#####################################################")
removedNode = myDoublyLL.nodeAt(3)
myDoublyLL.forwardPrint()
print("Node Removed : "+str(removedNode.element))