class Empleoyee:
    def __init__(self) -> None: # El primer método en ser llamado al momento de la creción. Constructor le dicen.
        self.name = "Leonardo"
    
    def printEmpleoyeeData(self):
        print(self.name)
        
    
    def welcomeMessageInstance(self):
        print(f"Welcome {self.name} to our organization")
    
    @staticmethod # Un método estático no toma el parámetro self por default, podríamos decir que son métodos de clase
    def welcomeMessageStatic():
        print(f"Welcome to our organization")


if __name__ == "__main__":
    emp = Empleoyee()
    emp.printEmpleoyeeData()
    emp.welcomeMessageInstance()
    emp.welcomeMessageStatic()