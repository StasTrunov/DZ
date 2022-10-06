from math import pi


class Figure:
    figure_name = ''
    S = 0
    def method_S(self):
        pass
        

class square(Figure):
    side = 0

    def method_S(self):
        S = self.side ** 2
        print(f'Назва фігури: {self.figure_name}. Длина сторони: {self.side}. Площа фігури: ',S)



class circle(Figure):
    radius = 0
    def method_S(self):
        S = pi * self.radius ** 2
        print(f'Назва фігури: {self.figure_name}. Длина сторони: {self.radius}. Площа фігури: ',S)



class rectangule(Figure):
    side_a = 0
    side_b = 0
    def method_S(self):
        S = self.side_a * self.side_b
        print(f'Назва фігури: {self.figure_name}. Длина сторони a: {self.side_a}. Длина сторони b: {self.side_b}. Площа фігури:',S)




Square_1 = square()
Square_1.figure_name = 'square_1'
Square_1.side = 7

Circle_1 = circle()
Circle_1.figure_name = 'circle_1'
Circle_1.radius = 10

Rectangule_1 = rectangule()
Rectangule_1.figure_name = 'square_1'
Rectangule_1.side_a = 6
Rectangule_1.side_b = 8

Square_1.method_S()
Circle_1.method_S()
Rectangule_1.method_S()