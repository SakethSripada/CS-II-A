class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def __str__(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"


class Student(Person):
    def __init__(self, name, age, grade, gpa):
        super().__init__(name, age)
        self.grade = grade
        self.gpa = gpa

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, gpa):
        self.__gpa = gpa

    def __str__(self):
        return f"Student: {self.name}, GPA: {self.gpa}"


class OfficeStaff(Person):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age)
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Office Staff: {self.name}, Position: {self.position}"


class CleaningStaff(Person):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age)
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Cleaning Staff: {self.name}, Position: {self.position}"


class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.street}, {self.city} {self.zip_code}"


teacher = Teacher("Lana", 35, "Math", 50000)
student = Student("James", 20, "Sophomore", 3.8)
staff = OfficeStaff("Alexa", 45, "Administrator", 40000)
cleaner = CleaningStaff("Mark", 30, "Janitor", 30000)
address = Address("123 Main St", "Dallas", "12345")

print(teacher)
print(student)
print(staff)
print(cleaner)
print(student.grade)
print(staff.position)
if teacher.salary > staff.salary:
    print(f"The teacher, {teacher.name}, has a higher salary than the office staff, {staff.name}.")
elif teacher.salary < staff.salary:
    print(f"The office staff, {staff.name}, has a higher salary than the teacher, {teacher.name}.")
else:
    print(f"The teacher, {teacher.name}, and the office staff, {staff.name}, have the same salary.")
