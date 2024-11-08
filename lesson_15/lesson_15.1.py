class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if isinstance(other, Rectangle):
            total_square = self.get_square() + other.get_square()
            new_width = max(self.width, other.width)
            new_height = total_square / new_width
            return Rectangle(new_width, new_height)
        else:
            raise TypeError("Працює тільки з об'єктами Rectangle")

    # ver_1 Збільшення тільки однієї сторони #
    # def __mul__(self, n):
    #     old_height = self.height
    #     new_width = self.width * n
    #     return Rectangle(old_height,new_width)

    # ver_2 Збільшення одразу 2 сторін, збереження пропорцій #
    def __mul__(self, n):
        scale = n / 2
        new_height = self.height * scale
        new_width = self.width * scale
        return Rectangle(new_height,new_width)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, square={self.get_square()})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print("Ok")
print(r3)