import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        string_r = f'{type(self).__name__}(width={self.width}, height={self.height})'
        return string_r

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2* (self.width + self.height))

    def get_diagonal(self):
        diagonal = math.sqrt(pow(self.width, 2)
                        + pow(self.height, 2))
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        r_pattern = ''
        for _ in range(self.height):
            for _ in range(self.width):
                r_pattern += '*'
            r_pattern += '\n'
        return r_pattern
        
    
    def get_amount_inside(self, shape):
        area_guest = shape.get_area()
        counter = 0
        area_home = self.get_area()
        while area_home >= area_guest:
            area_home = area_home - area_guest
            counter += 1
        return counter
    
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        string_s = f'{type(self).__name__}(side={self.width})'
        return string_s

    def set_side(self, side):
        self.width = side
        self.height = side


    
