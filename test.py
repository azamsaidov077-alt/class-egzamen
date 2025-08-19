class User:
    def __init__(self, name, phone, login, password, role):
        self.name = name
        self.phone = phone
        self.login = login
        self.password = password
        self.role = role



class Admin(User):
    def __init__(self, name, phone, login, password):
        super().__init__(name, phone, login, password, role="admin")

    def manage_teachers(self):
        pass

    def manage_groups(self):
        pass

    def manage_students(self):
        pass


class Teacher(User):
    def __init__(self, name, phone, login, password):
        super().__init__(name, phone, login, password, role="teacher")
        self.groups = []

    def view_my_groups(self):
        pass

    def view_my_students(self):
        pass

    def give_homework(self):
        pass


class Student(User):
    def __init__(self, name, phone, login, password):
        super().__init__(name, phone, login, password, role="student")
        self.homeworks = []
        self.grades = []

    def view_homeworks(self):
        pass

    def view_my_grades(self):
        pass


class Group:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.homeworks = []


class Homework:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.grades = {}
