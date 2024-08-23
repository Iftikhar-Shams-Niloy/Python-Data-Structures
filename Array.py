size = 5
array = [None]*size

print("Initializing the array:")
print(array)

print("Populating the array:")
array[0] = 10
array[1] = 20
array[2] = 30
array[3] = 40
print(array)

def shiftRight(array):
    for i in range(size):
        if i == (size-1):
            return
        elif i == 0:
            temp = array[i+1]
            array[i+1] = array[i]
            array[0]=None
        else:
            temp2 = array[i+1]
            array[i+1] = temp
            temp = temp2

def shiftLeft(array):
    for i in range(size):
        last_index = size-(i+1)
        if i == size-1:
            return
        elif last_index == (size-1):
            temp = array[last_index-1]
            array[last_index-1] = array[last_index]
            array[last_index] = None
        else:
            temp2 = array[last_index-1]
            array[last_index-1] = temp
            temp = temp2


shiftRight(array)
print("After Right Shift:\n",array)

shiftLeft(array)
print("After Left Shift:\n",array)

################# Circular Array #################
cir_array = [10,20,30,40,50]
startingIndex = 1
size = 5
