class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age

    def __str__(self):
        return f"{self.name}, {self.age}"

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    john = Student(name="Ali", age=21)
    bob = Student(name="Nodir", age=22)
    alice = Student(name="Vali", age=21)

    print(john > bob)
    print(john < bob)
    print(john == alice)
