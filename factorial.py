
def factorial(n):
    assert n>=0, "Just positive integers allowed"
    assert int(n) == n, "Just integers allowed"
    
    if n<2:
        return 1
    
    return n*factorial(n-1)


if __name__ == "__main__":
    
    print(factorial(0.0000001))