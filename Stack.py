# Making Stack using Array

class StackArray:
    stack = []
    pointer = -1
    def push(self, element):
        self.stack.append(element)
        self.pointer += 1
    def peek(self):
        return (self.stack[self.pointer])
    def pop(self):
        value = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return value

    def CheckParenthesis(self, string):
        err_check = False
        position = []
        paren_check1 = ["[", "{", "("]
        paren_check2 = ["]", "}", ")"]
        for i in range(len(string)):
            if string[i] in paren_check1:
                self.push(string[i])
                position.append(i+1)
            elif string[i] in paren_check2:
                if self.pointer > -1:
                    peek_check = self.peek()
                    if (peek_check=="("and string[i]==")") or (peek_check== "{"and string[i]=="}") or (peek_check=="["and string[i]=="]"):
                        self.pop()
                    else:
                        err_pos  = position[-1]
                        status = "Error at character #"+ str(err_pos) + ". '" +peek_check+ "'- not closed."
                        err_check = True

                    position = position[:-1]
                else :
                    err_pos = i+1
                    status = "Error at character #"+str(err_pos) + ". '" +string[i]+ "'- not opened."
                    err_check = True
                    break

        if err_check == True:
            print(string)
            print("This expression is NOT correct.")
            print(status)
        elif err_check == False:
            print(string)
            print("This expression is correct.")

# Making the Stack using Linked List

class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

class StackLinkedList():
    head = None
    elem_no = 0
    def push(self,elem):
        self.elem_no += 1
        if self.head == None:
            self.head = Node(elem)
        else:
            n = Node(elem)
            n.next = self.head
            self.head = n
    def peek(self):
        if self.head != None:
            return(self.head.element)
        else:
            return(None)
    def pop(self):
        self.elem_no -= 1
        temp = self.head
        self.head = self.head.next
        temp.element = None
        temp.next = None

    def CheckParenthesis(self, string):
        err_check = False
        position = []
        paren_check1 = ["[", "{", "("]
        paren_check2 = ["]", "}", ")"]
        for i in range(len(string)):
            if string[i] in paren_check1:
                self.push(string[i])
                position.append(i + 1)
            elif string[i] in paren_check2:
                head_check = self.peek()
                if self.elem_no == 0:
                    status = "Error at character #"+ str(i+1) + ". '" + string[i] + "'- not opened."
                    err_check = True
                    break
                else:
                    if (head_check=="("and string[i]==")") or (head_check== "{"and string[i]=="}") or (head_check=="["and string[i]=="]"):
                        self.pop()
                    else:
                        status = "Error at character #"+ str(position[-1]) + ". '" +head_check+ "'- not closed."
                        err_check = True
                    position = position[:-1]
        if err_check == True:
            print(string)
            print("This expression is NOT correct.")
            print(status)
        elif err_check == False:
            print(string)
            print("This expression is correct.")

