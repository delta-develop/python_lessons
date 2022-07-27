
def dec_to_bin(num):
    # remainder = num%2
    # num = num//2
    assert int(num) == num and num >= 0, "Only positive integers"
    
    if num == 0:
        return 0
    
    return num%2 + 10 * dec_to_bin(num//2)



for _ in range(8192*8):
    print(dec_to_bin(_))