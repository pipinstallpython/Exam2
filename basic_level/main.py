class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def set_first(self, value):
        self.first = value

    def set_second(self, value):
        self.second = value

    def get_product(self):
        return self.first * self.second


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_area(self):
        return self.width * self.height
