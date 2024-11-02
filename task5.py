import math


class Figure:
    # Статический атрибут класса, определяющий количество сторон (0 по умолчанию)
    sides_count = 0

    def __init__(self, color, sides):
        # Проверяем, если sides - это список
        if isinstance(sides, list) and len(sides) != self.sides_count:
            sides = [1] * self.sides_count  # Заполняем массив единицами
        elif isinstance(sides, int) and sides != self.sides_count:
            sides = [1] * self.sides_count  # Если передано целое число, заполняем массив единицами
        # Проверка и установка начального цвета
        if self.__is_valid_color(*color):
            self.__color = list(color)  # Сохранение цвета в виде списка RGB
        else:
            raise ValueError("Некорректное указание списка цветов. Пожалуйста, укажите цвет в формате RGB")

        # Проверка и установка начальных сторон, если они валидны
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)  # Сохранение списка сторон
        else:
            raise ValueError("Некорректное указание списка сторон.")

        # Публичный атрибут, указывающий, закрашена фигура или нет
        self.filled = False

    # Метод для получения текущего цвета фигуры
    def get_color(self):
        return self.__color

    # Статический метод для проверки корректности цвета
    @staticmethod
    def __is_valid_color(r, g, b):
        # Проверка, что каждый параметр (r, g, b) является целым числом и в диапазоне 0–255
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

        # Второй вариант написания проверки:
        # if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
        #     if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        #         return True
        # return False

    # Метод для установки нового цвета, если он корректный
    def set_color(self, r, g, b):
        # Проверяем, корректны ли введенные значения цвета
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]  # Обновляем цвет на новый
        else:
            print("Ошибка! Введены некорректные значения для цвета. Цвет остается прежним.")

    # Метод для получения списка сторон фигуры
    def get_sides(self):
        return self.__sides

    # Статический метод для проверки корректности сторон
    @staticmethod
    def __is_valid_sides(*sides):
        # Проверка, что каждая сторона — положительное целое число
        return all(isinstance(side, int) and side > 0 for side in sides)

        # Второй вариант написания проверки:
        # for side in sides:
        #     if not isinstance(side, int) or side <= 0:
        #         return False  # Если хотя бы одна сторона некорректна, вернуть False
        # return True

    # Метод для установки новых сторон, если их количество и значения корректны
    def set_sides(self, *new_sides):
        # Проверяем, что количество сторон соответствует sides_count и они валидны
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)  # Обновляем список сторон
        else:
            print("Ошибка! Количество или значения сторон некорректны, стороны не изменены.")

    # Метод для получения периметра фигуры (суммы всех сторон)
    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)

    # Метод для вычисления площади треугольника по формуле Герона
    def get_square(self):
        a, b, c = self.get_sides()  # Получаем длины сторон
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Формула Герона


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        if side_length <= 0:
            raise ValueError("Длина стороны должна быть положительным числом.")

        # Переопределяем __sides как список из 12 одинаковых сторон
        self._Figure__sides = [side_length] * self.sides_count  # Доступ к инкапсулированному атрибуту
        super().__init__(color, self._Figure__sides)  # Инициализируем родительский класс

    def get_volume(self):
        # Метод для вычисления объема куба
        return self.get_sides()[0] ** 3  # Объем куба V = a^3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())