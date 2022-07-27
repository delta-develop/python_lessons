
def sum_of_digits_1(n,sum=0):
    
    digits = str(n)
    factor = len(digits)
    sum += n % factor
    if factor == 1:
        return n
    
    return sum_of_digits_1(n,sum)
    

def sum_of_digits_2(n):
    assert int(n) == n and int(n) >= 0, "Only positive integers" 
    if int(n) == 0:
        return 0
    
    return int(n%10) + sum_of_digits_2(int(n//10))

def sum_of_digits_3(n):
    assert int(n) == n and int(n) >= 0, "Only positive integers"
    

print(sum_of_digits_2(11111111.5))