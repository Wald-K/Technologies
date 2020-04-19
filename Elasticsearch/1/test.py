from typing import TypeVar


class Student:
    def __init__(self, name: str):
        self.name: str = name
        self.teachers: list = []

    def __str__(self):
        return self.name

    def get_teachers(self) -> None:
        print(f'{self.name} teachers:')
        for teacher in self.teachers:
            print(teacher)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        teacher.students.append(self)


class Teacher:
    def __init__(self, name: str):
        self.name: str = name
        self.students: list = []

    def __str__(self):
        return self.name

    def get_students(self) -> None:
        print(f'{self.name} students:')
        for student in self.students:
            print(student)

    def add_student(self, student: Student):
        self.students.append(student)
        student.teachers.append(self)


s1 = Student('S1')
s2 = Student('S2')
s3 = Student('S3')

t1 = Teacher('T1')
t2 = Teacher('T2')

t1.add_student(s1)
t1.add_student(s2)

s1.add_teacher(t2)
s3.add_teacher(t2)

s3.get_teachers()
