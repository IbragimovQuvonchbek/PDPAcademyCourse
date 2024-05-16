class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def about(self):
        print("My name is", self.first_name,
              "and", self.last_name,
              "and", self.age)

    def __str__(self):
        return self.first_name


if __name__ == '__main__':
    student = Student("John", "Smith", 25)
    print(student)
