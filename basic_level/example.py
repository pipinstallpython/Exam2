from main import Pair, Rectangle

# Создание объекта Pair и вычисление произведения чисел
pair = Pair(3, 4)
print("Произведение чисел: ", pair.get_product())  # Выводит: 12

# Изменение полей Pair
pair.set_first(5)
pair.set_second(2)
print("Произведение чисел: ", pair.get_product())  # Выводит: 10

# Создание объекта Rectangle и вычисление периметра и площади
rectangle = Rectangle(5, 7)
print("Периметр: ", rectangle.get_perimeter())  # Выводит: 24
print("Площадь: ", rectangle.get_area())  # Выводит: 35

# Изменение полей Rectangle
rectangle.set_width(10)
rectangle.set_height(3)
print("Периметр: ", rectangle.get_perimeter())  # Выводит: 26
print("Площадь: ", rectangle.get_area())  # Выводит: 30

