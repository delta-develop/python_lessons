from random import randint
from time import time
import copy

def cronometer(func):
    def wrapper(*args):
        start = time()
        output = func(*args)
        end = time() - start
        print(f"Excecution time: {end}")
        return output
    return wrapper

@cronometer
def max_product(array):
    print("max_product: ",len(array))
    print(array)
    array = set(array)
    array = list(array)
    array.sort()
    print(array)
    return array[-1] * array[-2]

@cronometer
def max_product_alt(array):
    print(array)
    print("max_product_alt: ",len(array))
    array = set(array)
    array = list(array)
    array.sort()
    
    first_max = max(array)
    second_max = max(array[:-1])
    return first_max * second_max
    
def are_unique(array):
    array_set = set(array)
    if len(array) == len(array_set):
        return True
    return False

my_array = [randint(0,100) for _ in range(200)]
array_copy = copy.deepcopy(my_array)
print(max_product(my_array))
print(max_product_alt(my_array))
print(are_unique(my_array))
unique = list(set(my_array))
print(are_unique(unique))
