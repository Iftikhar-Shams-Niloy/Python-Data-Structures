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
                n = Node(array[i], None)
                tail.next = n
                tail = tail.next
        else:
            self.head = a


    def countNode(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def printList(self):
        temp = self.head
        while temp != None:
            if temp.next != None:
                print(temp.element, end=", ")
            else:
                print(temp.element)
            temp = temp.next

    def nodeAt(self, idx):
        temp = self.head
        count = 0
        flag = 0
        none_node = Node(None, None)
        while temp != None:
            if count == idx:
                flag = temp
            count += 1
            temp = temp.next
        if flag == 0:
            flag = none_node
        return flag

    def get(self, idx):
        temp = self.head
        count = 0
        give = 0
        none_node = Node(None, None)
        while temp != None:
            if count == idx:
                give = temp.element
            count += 1
            temp = temp.next
        if give == 0:
            give = none_node.element
        return give

    def set(self, idx, elem):
        temp = self.head
        count = 0
        give = 0
        none_node = Node(None, None)
        while temp != None:
            if count == idx:
                give = temp.element
                temp.element = elem
            count += 1
            temp = temp.next
        if give == 0:
            give = none_node.element
        return give

    def indexOf(self, elem):
        count = 0
        temp = self.head
        idx = -1
        while temp != None:
            if temp.element == elem:
                idx = count
            temp = temp.next
            count += 1
        return idx

    def contains(self, elem):
        temp = self.head
        has = False
        while temp != None:
            if temp.element == elem:
                has = True
            temp = temp.next
        return has

    def copyList(self):
        new_head = Node(self.head.element, None)
        tail = new_head
        temp = self.head.next
        while temp != None:
            n = Node(temp.element, None)
            tail.next = n
            tail = tail.next
            temp = temp.next
        return new_head

    def reverseList(self):
        new_head = Node(self.head.element, None)
        temp = self.head.next
        while temp != None:
            n = Node(temp.element, new_head)
            new_head = n
            temp = temp.next
        return new_head

    def insert(self, elem, idx):
        n = Node(elem, None)
        if  self.countNode() > idx > 0:
            n1 = self.nodeAt(idx)
            n2 = self.nodeAt(idx - 1)
            n.next = n1
            n2.next = n
        elif idx == 0:
            n1 = self.nodeAt(idx)
            n.next = n1
            self.head = n
        elif idx == self.countNode():
            n1 = self.nodeAt(idx-1)
            n1.next = n

    def remove(self, idx):
        count = 0
        temp = self.head
        while temp != None:
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
            temp = temp.next

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
