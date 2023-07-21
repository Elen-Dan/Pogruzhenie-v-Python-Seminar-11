'''
Задание № 5
- Дорабатываем класс прямоугольник из прошлого семинара.
- Добавьте возможность сложения и вычитания.
- При этом должен создаваться новый экземпляр прямоугольника.
- Складываем и вычитаем периметры, а не длину и ширину.
- При вычитании не допускайте отрицательных значений.
'''

class Rectangle:
    '''Создание класса прямоугольника
    '''
    def __init__(self, width: float, height: float = None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def calc_perimeter(self):
        '''расчет периметра прямоугольника
        '''
        return (self.width + self.height) * 2

    def calc_area(self):
        '''расчет площади прямоугольника
        '''
        return self.width * self.height

    def __add__(self, other):
        '''сложение периметров прямоугольника
        '''
        perimetr = self.calc_perimeter() + other.calc_perimeter()
        width = self.width + other.width
        height = perimetr/2 - width
        return Rectangle(width, height)
    
    def __sub__(self, other):
        '''вычитание периметров прямоугольника
        '''
        if self.calc_perimeter() < other.calc_perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimetr = self.calc_perimeter() - other.calc_perimeter()
        height = perimetr/2 - width
        return Rectangle(width, height)

    def __str__(self):
        return f'периметр = {self.calc_perimeter()}, длина = {self.width}, высота = {self.height}'

if __name__ == '__main__':
    new_rect = Rectangle(10, 20)
    print(new_rect.calc_area())
    print(new_rect.calc_perimeter())

    new_square = Rectangle(10)
    print(new_square.calc_area())
    print(new_square.calc_perimeter())

    print(new_rect == new_square)

    print(Rectangle.__doc__)
    print(Rectangle.calc_perimeter.__doc__)
    print(Rectangle.calc_area.__doc__)
    print(Rectangle.__add__.__doc__)
    print(Rectangle.__sub__.__doc__)