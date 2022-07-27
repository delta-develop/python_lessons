

def power(n,pow):
    assert int(pow) == pow and pow>=0, "Only positive integer pow "
    if pow == 0:
        return 1
    return n*power(n,pow-1)


print(power(2,1))