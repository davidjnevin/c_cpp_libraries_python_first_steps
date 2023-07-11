import ctypes

# Passing and returning c_char_p strings

print("=" * 20)
clibrary = ctypes.CDLL(
    "/Users/Communitymanager-work/Google Drive/code/ctypes_tutorial/clibrary.so"
)

func = clibrary.display
func.argtypes = [ctypes.c_char_p, ctypes.c_int]  # Many args possible
func.restype = ctypes.c_char_p  # but only one return type.
func(b"David", 46)

# Passing and returning c_int ints

print("\n")
print("=" * 20)
clibrary_add = ctypes.CDLL(
    "/Users/Communitymanager-work/Google Drive/code/ctypes_tutorial/clibrary_add.so"
)

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

clibrary_pointers = ctypes.CDLL(
    "/Users/Communitymanager-work/Google Drive/code/ctypes_tutorial/clibrary_pointers.so"
)

alloc_func = clibrary_pointers.alloc_memory
alloc_func.restype = ctypes.POINTER(ctypes.c_char_p)

free_func = clibrary_pointers.free_memory
free_func.argtypes = [ctypes.POINTER(ctypes.c_char_p)]

cstring_pointer = alloc_func()

cstring = ctypes.c_char_p.from_buffer(cstring_pointer)
print(cstring.value)
free_func(cstring_pointer)
