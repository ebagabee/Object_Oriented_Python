class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        x1 = self.__x1
        x2 = self.__x2
        return x2 if x2 < x1 else x1

    def get_right_x(self):
        x1 = self.__x1
        x2 = self.__x2
        
        return x1 if x1 > x2 else x2 

    def get_top_y(self):
        y1 = self.__y1
        y2 = self.__y2
        
        return y2 if y2 > y1 else y1 

    def get_bottom_y(self):
        y1 = self.__y1
        y2 = self.__y2
        
        return y1 if y1 < y2 else y2 

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
