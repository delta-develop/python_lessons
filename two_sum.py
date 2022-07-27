from time import time
from random import randrange

def cronometer(func):
    def wrapper(*args):
        start = time()
        output = func(*args)
        end = time() - start
        print(f"Excecution time: {end}")
        return output
    return wrapper
        

# @cronometer
# def two_sum_for(arr, obj):
#     pos1,pos2 = None, None
#     solutions = []
#     for index,item in enumerate(arr):
#         difference = obj - item
#         if difference in arr:
#             pos1 = index
#             pos2 = arr.index(difference)
#             if (pos2,pos1) not in solutions: 
#                 solutions.append((pos1,pos2))
    
#     return solutions

# @cronometer
# def two_sum_while(arr, obj):
#     pos1,pos2 = None, None
#     solutions = []
#     index = 0
#     while index <= (len(arr)/2) + 1:
#         difference = obj - arr[index]
#         if difference in arr:
#             pos1 = index
#             pos2 = arr.index(difference)
#             if (pos2,pos1) not in solutions: 
#                 solutions.append((pos1,pos2))
#         index += 1
#     return solutions


@cronometer
def two_sum_for(arr, obj):
    solutions = []
    for item in arr:
        difference = obj - item
        if difference in arr:
            if (difference,item) not in solutions: 
                solutions.append((item,difference))
    
    return solutions

@cronometer
def two_sum_while(arr, obj):
    solutions = []
    index = 0
    while index <= (len(arr)/2):
        
        number = arr[index]
        difference = obj - number
        if difference in arr:
            if (difference,number) not in solutions: 
                solutions.append((number,difference))
        index += 1
    return solutions




if __name__ == "__main__":
    arr = {randrange(0,100000) for _ in range(100000)}
    
    obj = randrange(0,200000)
    print(f"OBJECTIVE -->> {obj}")
    # print("arr")
    # print(arr)
    # print("")
    solutions_2 = two_sum_for(arr,obj)
    solutions_1 = two_sum_while(arr,obj)
    print(len(solutions_1))
    print(len(solutions_2))