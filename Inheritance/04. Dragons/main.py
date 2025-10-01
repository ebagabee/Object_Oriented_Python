class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        # Meu X tem que ser maior que o x inicial e menor que o x final
        # Meu Y tem que ser maior que o y inicial e menor que o y final
        return x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        r = self.__fire_range
        x_1 = x - r
        x_2 = x + r
        y_1 = y - r
        y_2 = y + r 

        in_area = []

        for unit in units:
            if unit.in_area(x_1, y_1, x_2, y_2):
                in_area.append(unit)

        return in_area
            
        

       
            
