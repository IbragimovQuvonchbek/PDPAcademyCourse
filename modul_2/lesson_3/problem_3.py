class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}"


class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}, Subject: {self.subject}"


class Assistant(Teacher):
    def __init__(self, name, email, subject, teacher_name):
        super().__init__(name, email, subject)
        self.teacher_name = teacher_name

    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}, Subject: {self.subject}, Assisting Teacher: {self.teacher_name}"


class Mentor(Teacher):
    def __init__(self, name, email, subject, experience):
        super().__init__(name, email, subject)
        self.experience = experience

    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}, Subject: {self.subject}, Experience: {self.experience} years"


user = User("Alice", "alice@example.com")
print(user.get_info())

teacher = Teacher("Bob", "bob@example.com", "Python")
print(teacher.get_info())

mentor = Mentor("Charlie", "charlie@example.com", "Java", 10)
print(mentor.get_info())

assistant = Assistant("David", "david@example.com", "C#", "Dr. Smith")
print(assistant.get_info())
