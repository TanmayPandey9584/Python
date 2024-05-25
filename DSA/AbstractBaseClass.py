from abc import ABC , abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(shape):
    type= "rectangle"
    def __init__(self):
        self.length = 4
        self.breadth = 5
    def printarea(self):
        return self.length*self.breadth
    
rect=rectangle()
print(rect.printarea())