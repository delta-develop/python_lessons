def openRussianDoll(doll):
    if doll == 1:
        print("All dolls opened")
    else:
        print(f"Doll {doll}")
        openRussianDoll(doll-1)
    

def fibonacci(number):
    for i in range(number): 
        if i < 2:
            print(i)
        else:
            return fibonacci(i-2) + fibonacci(i-1)

    

if __name__ =="__main__":
    dolls = 10
    # openRussianDoll(dolls)
    for _ in range(10):
        print(fibonacci(_))