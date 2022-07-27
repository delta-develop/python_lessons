# Pairs must be distinct
from random import randint
from time import time

def cronometer(func):
    def wrapper(*args):
        start = time()
        output = func(*args)
        end = time() - start
        print(f"Excecution time: {end}")
        return output
    return wrapper

@cronometer
def findPair(nums, target):
    count = 0
    for i in range(len(nums)):
        if nums[i]> target:
            continue
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                # print(f"i: {i} = {nums[i]} j: {j} = {nums[j]}")
                count += 1
    
    print(count)
            

@cronometer
def find_pair_efficient(nums,target):
    nums.sort()
    nums = set(nums)
    nums = list(nums)
    count = 0
    for i in range(len(nums)):
        if nums[i] > target:
            break
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[j] > target:
                break
            elif nums[i] + nums[j] == target:
                # print(f"i: {i} = {nums[i]} j: {j} = {nums[j]}")
                count += 1
                
    print(count)

    

my_list = [randint(0,1000) for _ in range(randint(0,100000))]
target = randint(0,1000)
print("Target:",target)
findPair(my_list, target)
find_pair_efficient(my_list,target)