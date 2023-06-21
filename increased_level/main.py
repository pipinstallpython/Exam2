class Pair:
    def __init__(self, first, second):
        if isinstance(first, float) and first > 0 and isinstance(second, int) and second > 0:
            self.first = first
            self.second = second
        else:
            raise ValueError("Некорректные значения полей")

    def cost(self):
        return self.first * self.second

    def display(self):
        print(f"Цена: {self.first}, Количество: {self.second}")

    @staticmethod
    def read():
        first = float(input("Введите цену товара: "))
        second = int(input("Введите количество товара: "))
        return Pair(first, second)


def make_Pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(e)
        return None
