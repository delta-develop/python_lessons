class Empleoyee:
    
    def empleoyeeDetails(self):
        self.name = "Leonardo"
        print(self.name)
        # age = 29 # Esta variable vivirá en el scope de su función, pero eso no la hace 
                #  parte de los atributs de la instancia
        
        self.age = 29
    
    def printEmpleoyeeDetails(self):
        print(f"Nombre: {self.name}, edad: {self.age}")

empleoyee = Empleoyee()
empleoyee.empleoyeeDetails() # Esto cuenta como pasar un argumento, la instancia de clase pasa como argumento
Empleoyee.empleoyeeDetails(empleoyee) # Esta línea es equivalente a la anterior
empleoyee.printEmpleoyeeDetails()