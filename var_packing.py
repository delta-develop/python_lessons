


def single_unpack(*items):
    for item in items:
        print(item, end=" ")
    
    print()
        

def double_unpack(**items):
    for key,value in items.items():
        print(f"key: {key} value: {value}")
        

if __name__ == "__main__":
    
    single_unpack(1,2,3,4,"alpha","beta","gamma","delta")
    double_unpack(first="first value",second="second value",third=3,fourth=None)        