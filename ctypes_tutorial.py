import ctypes
import os

# Passing and returning c_char_p strings

print("=" * 20)

path = os.getcwd()  # set the local path
clibrary = ctypes.CDLL(os.path.join(path, "clibrary.so"))

func = clibrary.display  # define the function
func.argtypes = [ctypes.c_char_p, ctypes.c_int]  # Many args possible
func.restype = ctypes.c_char_p  # but only one return type.
func(b"David", 46)

# Passing and returning c_int ints

print("\n")
print("=" * 20)
clibrary_add = ctypes.CDLL(os.path.join(path, "clibrary_add.so"))

func_2 = clibrary_add.add
func_2.argtypes = [ctypes.c_int, ctypes.c_int]  # Many args possible
func_2.restype = ctypes.c_int  # but only one return type.

num1 = 18
num2 = 36
addition = func_2(num1, num2)
print("\n")
print(f"The sum {num1} and {num2} is: ", addition)
print("\n")

# Allocating and freeing memory via POINTER

print("=" * 20)
print("\n")

clibrary_pointers = ctypes.CDLL(os.path.join(path, "clibrary_pointers.so"))

alloc_func = clibrary_pointers.alloc_memory
alloc_func.restype = ctypes.POINTER(ctypes.c_char_p)

free_func = clibrary_pointers.free_memory
free_func.argtypes = [ctypes.POINTER(ctypes.c_char_p)]

cstring_pointer = alloc_func()

cstring = ctypes.c_char_p.from_buffer(cstring_pointer)  # use a buffer for the string
print(cstring.value)
free_func(cstring_pointer)

# Using pointers

print("=" * 20)
print("\n")

num = ctypes.c_int(100)  # create a ctypes int
ptr = ctypes.pointer(num)  # create a pointer to the int

print(ptr.contents)  # dereference the pointer to get the value

## Using factory function to create a new ctypes type.

ptr2 = ctypes.POINTER(ctypes.c_int)  # create a new ctypes type

ptr2.contents = num  # assign the value to the new type
print(ptr2.contents)  # dereference the pointer to get the value

# ctypes.POINTER(type): This function is a factory function that creates a new ctypes type. It doesn't create a pointer; it creates a new type that can represent pointers to a particular other type.
# ctypes.pointer(obj): This function actually creates a pointer to an existing ctypes object. For example, if i is a ctypes.c_int instance, then ctypes.pointer(i) returns a pointer to i.

# Using Arrays
# Use an array sum library written in c

print("=" * 20)
print("\n")

# create and array of c_ints, default value is zero and then set to 0, 1, 2, 3, ...
# and pass it to c

values = (ctypes.c_int * 10)()  # create an array of 10 c_ints
for i in range(len(values)):  # set the values
    values[i] = i

path = os.getcwd()
clibrary_array_sum = ctypes.CDLL(os.path.join(path, "clibrary_array_sum.so"))

sum = clibrary_array_sum.sumArray(values, len(values))  # pass the array to c
print("This sum is calculated and returned from a c library: ", sum)  # print the result


print("=" * 20)
print("\n")

# create an array in c and pass it to python
print([x for x in values])  # print the array
clibrary_array_inc = ctypes.CDLL(
    os.path.join(path, "clibrary_array_inc.so")
)  # load the library


clibrary_array_inc.incArray.restype = ctypes.POINTER(
    ctypes.c_int
)  # set the return type

new_array = clibrary_array_inc.incArray(values, len(values))  # pass the array to c

for i in range(len(10)):
    print(new_array[i])
