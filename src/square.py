class Square: 

    # FIXME
    def __init__(self, side) -> None:
        if side <= 0:
            self.side = 1 
        else:
            self.side = side

    def area(self): 
        return self.side * self.side 
    
    # FIXME
    def perimeter(self): 
        return self.side * 4