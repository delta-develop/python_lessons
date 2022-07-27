from time import time

def cronometer(func):
    def wrapper(*args):
        start = time()
        output = func(*args)
        end = time() - start
        print(f"Excecution time: {end}")
        return output
    return wrapper


def fibo(n):
    
    assert n>=0, "Only positive numbers"
    assert int(n) == n, "Only integers allowed"
    
    if n in [0,1]:
        return n
    
    return fibo(n-1) + fibo(n-2)


def fibo_mem(n,memory={}):
    
    assert n>=0, "Only positive numbers"
    assert int(n) == n, "Only integers allowed"
    
    if n in [0,1]:
        return n
    
    if not f"{n-1}" in memory:
        memory[f"{n-1}"] = fibo_mem(n-1,memory)
        
    n_1 = memory[f"{n-1}"]
        
    
    if not f"{n-2}" in memory:
        memory[f"{n-2}"] = fibo_mem(n-2,memory)
        
    n_2 = memory[f"{n-2}"]
        
        
    # print(memory)
    
    return n_1 + n_2   

def fibo_seq(n_goal,n_minus_2=0,n_minus_1=1):
    
    if n_minus_2 == 0:
        print(n_minus_2)
        print(n_minus_1)
        
    n = n_minus_1 + n_minus_2
    print(n)
    
    if n >= n_goal:
        return
    
    n_minus_2 = n_minus_1
    n_minus_1 = n
    
    
    return fibo_seq(n_goal,n_minus_2,n_minus_1)
        

if __name__ == "__main__":
    start = time()
    print(fibo(30))
    end = time() - start
    print(f"Excecution time: {end}")
    
    start = time()
    print(fibo_mem(450))
    end = time() - start
    print(f"Excecution time: {end}")