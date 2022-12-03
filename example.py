from math import sqrt

message: str = 'Добро пожаловать в самую лучшую программу для вычисления ' \
               'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Number: float):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: float):
    """Ввод вашего числа."""
    if your_number <= 0:
        return CalculateцуSquareRoot(your_number)
    Calculate = CalculateSquareRoot(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {Calculate}')


calc(25.5)
