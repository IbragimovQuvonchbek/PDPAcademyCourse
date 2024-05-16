class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(2, 4)

    v3 = v1 - v2
    print(v3)
