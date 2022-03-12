
class Vector:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    
    def __add__(self, vector2):
        
        x = self.x + vector2.x
        y = self.y + vector2.y
        return Vector(x,y)

    def __iadd__(self,vector2):
        self.x += vector2.x
        self.y += vector2.y
        return self
        
    
    def __str__(self):
        return f"x:{self.x}, y:{self.y}"

if __name__ == "__main__":
    v1 = Vector(2,4)
    v2 = Vector(5,3)
    v3 = v1 + v2
    print(v3)