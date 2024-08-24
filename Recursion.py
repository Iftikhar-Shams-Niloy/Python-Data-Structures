def recursivePrintNumber(int):
    if int <= 0:
        print("Last Number Reached")
    else:
        recursivePrintNumber(int - 1)
        if int % 2 == 0:
            print(int)


def recursiveReversePrintNumber(int):
    if int <= 0:
        return
    else:
        print(int)
        recursiveReversePrintNumber(int-1)

def recursiveSelectionSort(arr, arr_len, idx=0):
    def mini_index(arr, idx1, idx2):
        if idx1 == idx2:
            return idx1
        mini = mini_index(arr, idx1 + 1, idx2)
        if arr[idx1] < arr[mini]:
            return idx1
        else:
            return mini

    if idx == arr_len:
        return -1
    mini = mini_index(arr, idx, arr_len - 1)

    if mini != idx:
        arr[idx], arr[mini] = arr[mini], arr[idx]
    recursiveSelectionSort(arr, arr_len, idx + 1)

def rearrange(arr, idx=1, comparing=None):
    if idx >= 0 :
        if comparing < arr[idx]:
            arr[idx+1] = arr[idx]
            arr[idx] = comparing #comparing = 11
            rearrange(arr, idx-1, comparing)
    else:
        return
def recursiveInsertionSort(arr, idx=1, comparing=None):
    if idx >= 1 and idx < len(arr):
        comparing = arr[idx]
        new_idx = idx-1
        rearrange(arr, new_idx, comparing)
        recursiveInsertionSort(arr, idx+1, comparing)
    else:
        return

cache = [None]*10

def nth_fib(n):
    if n <= 1:
        return n
    else:
        return nth_fib(n-1) + nth_fib(n-2)

#################################################################
##########################  START   ############################
#################################################################
flag = False
def addEven(array, idx=None, sum=0):
    if idx == None:
        idx = len(array)-1

    if idx >= 0 :
        if array[idx]%2 == 0:
            sum += array[idx]
        addEven(array, idx-1, sum)
    else:
        return "Sum of even numbers:",sum

##############################################################
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

def multiplyOdd(head, total=0):
    if head.element%2 == 1:
        if total == 0:
            total = head.element
        else:
            total *= head.element

    if head.next == None:
        print(total)
        return total
    else:
        head = head.next
        multiplyOdd(head,total)

#########################################################

def recursiveFactorial(num):
    if num <= 0 :
        return 1
    else :
        return num * recursiveFactorial(num-1)

def nCr(n, r):
    if r == 0 or n == r:
        return 1
    else:
        result = recursiveFactorial(n) / (recursiveFactorial(r) * recursiveFactorial(n-r))
        print(result)

#########################################################






my_array = [2,3,7,9,3]
# my_sum = addEven(my_array)
# print(my_sum)

my_LL = LinkedList(my_array)
multiplyOdd(my_LL.head)


# nCr(10,3)
#
# recursivePrintNumber(10)


