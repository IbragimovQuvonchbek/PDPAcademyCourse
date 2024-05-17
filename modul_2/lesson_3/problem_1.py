class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        first_name, last_name = full_name.split(' ', 1)
        return cls(first_name, last_name)


if __name__ == '__main__':
    student = Student.from_full_name('John Smith')
    print(student.first_name)  # 'John'
    print(student.last_name)  # 'Smith'
