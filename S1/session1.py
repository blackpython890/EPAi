def myfunc():
    string = 'Cppsecrets'
    n=len( string )
    arr=[]
    for i in range( n ):
        for j in range( i+1, n+1 ):
            a = string[ i:j ]
            arr.append(a)
    
    
    print(arr)


def my_func():
    pass


class Rectangle:
    '''
        This is a Rectangle Class. 
        1. If r = Rectangle(10, 20), 
        then >>>r gives 'Rectangle(10, 20)' as it's output
        2. And print(r) gives 'Rectangle: width=10, height=20' as the print output.
        3. Raises Value error if one tries to set width or height as negative
        4. Raises NotImplementedError if one tries to check for r1 < r2, and r2 is not a Rectangle Object
    '''
    def __init__(self, width, height):
        self._width = width #properties
        self._height = height 
    
    @property
    def width(self):
        return self._width
    
    
    @width.setter
    def width(self, width):
        if self._width <=0 :
            raise e_info ("Width must be positive")
        else:
            self._width = width
    
    
    @property
    def height(self):
        return self._height
    
    
    @height.setter
    def height(self, height):
        if self._height <=0:
            raise e_info ("Height must be positive")
        else:
            self._height = height
    
    
    def area(self): #method
        return self._width * self._height
    
    
    def perimeter(self):
        return 2*(self._width + self._height)
    
    
    def __repr__(self):
        return f'Rectangle({self._width}, {self._height})'
    
    
    def __str__(self):
        return f'Rectangle: width={self.width}, height={self.height}'
        
        
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented
    
    def __eq__(self,other):
        if  isinstance(other,Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False
    
    def __com__(self,other):
        if not isintance(other,Rectangle):
            raise NotImplemented
        else:
            return self.area() < other.area()