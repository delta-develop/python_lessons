# lambda input, parameters: operation+to+return
# (lambda input, parameters: operation+to+return)(in, line, given, values)


if __name__ == "__main__":
    a = 10
    b = 20
    print(f"Variables afuera: {(lambda a,b : a + b)(a,b)}")
    print(f"Variables dentro: {(lambda c=20,d=30 : c - d)()}")
    print(f"Variables a un lado: {(lambda e,f : e * f)(5,4)}")
    print(f"Variables empaquetadas: {(lambda *args : sum(args))(1,2,3,4,5,6,7,8,9,10)}")
    
    
    