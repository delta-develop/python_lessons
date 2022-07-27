
def is_palindrom_recursive(word):
    first, *inner, last = word
    
    print("inner",inner)
    if first != last
        return False
    
    if len(inner) > 1:
        return is_palindrom_recursive(inner)
    
    return True

def is_palindrom_iterative(word):
    inner = word
    
    while len(inner) > 1:
        
        first, *inner, last = inner
        print("inner",inner)
        
        if first != last:
            return False
    
    return True
    

if __name__ == "__main__":
    some_words =["Leonardo","anita lava la tina","qwewq","qwerewq","qweewq"]
    
    # x = map(is_palindrom,some_words)
    
    # print(list(x))
    
    for word in some_words:
        print(word,is_palindrom_recursive(word))
        
    print("\n")
    
    for word in some_words:
        print(word,is_palindrom_iterative(word))