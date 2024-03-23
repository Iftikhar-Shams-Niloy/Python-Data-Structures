class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n


class LinkedList:
    def __init__(self, a):
        array = a
        if type(array) == list:
            self.head = Node(array[0], None)
            tail = self.head
            for i in range(1, len(array)):
                new_node  = Node(array[i], None)
                tail.next = new_node
                tail = tail.next
        else:
            self.head = a


    def countNode(self):
        count = 0
        pointer = self.head
        while pointer != None:
            count += 1
            pointer = pointer.next
        i=count
        return i

    def printList(self):
        pointer = self.head
        while pointer != None:
            if pointer.next != None:
                print(pointer.element, end=", ")
            else:
                print(pointer.element)
            pointer = pointer.next

    def nodeAt(self, idx):
        pointer = self.head
        count = 0
        flag = 0
        none_node = Node(None, None)
        while pointer != None:
            if count == idx:
                flag = pointer
            count += 1
            pointer = pointer.next
        if flag == 0:
            flag = none_node
        return flag

    def get(self, idx):
        pointer = self.head
        count = 0
        give = 0
        none_node = Node(None, None)
        while pointer != None:
            if count == idx:
                give = pointer.element
            count += 1
            pointer = pointer.next
        if give == 0:
            give = none_node.element
        return give

    def set(self, idx, elem):
        pointer = self.head
        count = 0
        give = 0
        none_node = Node(None, None)
        while pointer != None:
            if count == idx:
                give = pointer.element
                pointer.element = elem
            count += 1
            pointer = pointer.next
        if give == 0:
            give = none_node.element
        return give

    def indexOf(self, elem):
        count = 0
        pointer = self.head
        idx = -1
        while pointer != None:
            if pointer.element == elem:
                idx = count
            pointer = pointer.next
            count += 1
        return idx

    def contains(self, elem):
        pointer = self.head
        has = False
        while pointer != None:
            if pointer.element == elem:
                has = True
            pointer = pointer.next
        return has

    def copyList(self):
        new_head = Node(self.head.element, None)
        tail = new_head
        pointer = self.head.next
        while pointer != None:
            n = Node(pointer.element, None)
            tail.next = n
            tail = tail.next
            pointer = pointer.next
        return new_head

    def reverseList(self):
        new_head = Node(self.head.element, None)
        pointer = self.head.next
        while pointer != None:
            n = Node(pointer.element, new_head)
            new_head = n
            pointer = pointer.next
        return new_head

    def insert(self, elem, idx):
        new = Node(elem, None)
        if  self.countNode() > idx > 0:
            n1 = self.nodeAt(idx)
            n2 = self.nodeAt(idx - 1)
            new.next = n1
            n2.next = new
        elif idx == 0:
            n1 = self.nodeAt(idx)
            new.next = n1
            self.head = new
        elif idx == self.countNode():
            n1 = self.nodeAt(idx-1)
            n1.next = new

    def remove(self, idx):
        count = 0
        pointer = self.head
        while pointer != None:
            if count == idx:
                if count == 0:
                    removed = self.head.element
                    self.head = self.head.next
                    return removed
                elif count > 0:
                    n1 = self.nodeAt(idx-1)
                    n2 = self.nodeAt(idx+1)
                    n_removed = self.nodeAt(idx)
                    n1.next = n2
                    return n_removed.element
                elif count == (self.countNode()-1):
                    n1 = self.nodeAt(idx-1)
                    n1.next = None
                    n_removed = (self.nodeAt(idx))
                    return n_removed.element
            count += 1
            pointer = pointer.next

    def rotateLeft(self):
        old_head = self.head
        last_node = old_head

        while old_head.next is not None:
            old_head = old_head.next
        old_head.next = self.head
        self.head = last_node.next
        last_node.next = None

    def rotateRight(self):
        new_next = self.head
        rang = self.countNode()-1
        new_tail = self.countNode()-2

        last_node = self.nodeAt(rang)
        before_last_node = self.nodeAt(new_tail)

        last_node.next = new_next
        self.head = last_node
        before_last_node.next = None


# Test Example
my_linked_list = LinkedList([1,2,3,4,5])
my_linked_list.printList()
print(my_linked_list.countNode())
node = my_linked_list.nodeAt(2)
print(node.element)
print("#########################")
my_linked_list.set(2,99)
my_linked_list.printList()
print("#########################")
my_linked_list.insert(911, 1)
my_linked_list.printList()