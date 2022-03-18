
class Vector:
    def __init__(self,*args, **kwargs):
        self.components = []
        try:
            for arg in args:
                self.components.append(arg)
        except Exception as e:
            print(e)
        
    
    def __add__(vector1, vector2):
        
        if len(vector1.components) != len(vector2.components):
            raise Exception("Dimentional error")

        resultant_vector = Vector()
        for vector_1_comp, vector_2_comp in zip(vector1.components, vector2.components):
            resultant_vector.append(vector_1_comp + vector_2_comp)
        
        return resultant_vector

    def __repr__(self) -> str:
        return f"{self.components}"


    def append(self,value):
        if isinstance(value,int) or isinstance(value,float):
            self.components.append(value)
        else:
            raise Exception("Invalid value")
    
    
    def __str__(self):
        return f"{self.components}"

if __name__ == "__main__":
    v1 = Vector(1,2,3)
    v2 = Vector(-1,-2,-3)
    v3 = v1 + v2
    print(v3)
    v3 += v1
    print(v3)
    
    