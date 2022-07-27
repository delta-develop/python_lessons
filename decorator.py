

def decorator(func):
    def wrapper():
        print("pre-function")
        output = func()
        print("post-function")
        return output
    return wrapper


def decorator_2(func):
    print("pre_function")
    output = func()
    print("post_function")
    return output


def my_function():
    print("my_function")
    
    
if __name__ == "__main__":
    def my_function():
        print("my_function")
    
    decorator(my_function)