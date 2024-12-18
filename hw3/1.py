class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        print("Модуль:",(self.x**2 + self.y**2 + self.z**2)**0.5)
    def sum(self, x, y, z):
        print("Cумма векторов:", self.x + x, self.y + y, self.z + z)
    def dif(self, x, y, z):
        print("Разность векторов:", self.x - x, self.y - y, self.z - z)
    def scal(self, x, y, z):
        print("Скалярное произведение векторов:", self.x * x + self.y * y + self.z * z)
    def prod(self, k):
        print("Умножение вектора на число:", self.x * k, self.y * k, self.z * k)

Vector(1, 2, 3).__abs__()
Vector(1, 2, 3).sum(4, 5, 6)
Vector(1, 2, 3).dif(4, 5, 6)
Vector(1, 2, 3).scal(4, 5, 6)
Vector(1, 2, 3).prod(4)
