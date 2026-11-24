"""
OOP concept	Koddagi joyi
Class & Object	Person, Student
Constructor	__init__()
Ordinary property	self.name
Static property	university
Instance method	study()
Special method	__str__(), __repr__()
Class method	change_university()
Static method	is_adult()
Inheritance	Student(Person)
Encapsulation	__gpa, getter, setter
Polymorphism	person.introduce()
"""


# ============================================================
# UNIVERSITY MANAGEMENT SYSTEM
# ============================================================
# This project demonstrates Object-Oriented Programming (OOP)
# concepts using a simple university management system.
#
# Main concepts:
# 1. Class and Object
# 2. Constructor (__init__)
# 3. Ordinary and Static Properties
# 4. Instance Methods
# 5. Special Methods (__str__, __repr__)
# 6. Class Methods (@classmethod)
# 7. Static Methods (@staticmethod)
# 8. Inheritance
# 9. Encapsulation
# 10. Polymorphism
# ============================================================


# ============================================================
# 1. PERSON CLASS
# ============================================================
# A class is a blueprint used to create objects.
#
# Person is the parent class.
# Both Student and Teacher will inherit its properties
# and methods.
# ============================================================

class Person:

    # --------------------------------------------------------
    # Static property (Class Variable)
    # --------------------------------------------------------
    # This variable belongs to the class itself.
    # All Person objects share the same university name.
    # It can be accessed using Person.university.
    # --------------------------------------------------------

    university = "Global University"

    # --------------------------------------------------------
    # Constructor
    # --------------------------------------------------------
    # __init__ is a special method.
    # Python automatically calls it when a new object is created.
    #
    # self refers to the current object.
    # name, age and email are parameters.
    #
    # self.name, self.age and self.email are ordinary
    # instance properties. Each object has its own values.
    # --------------------------------------------------------

    def __init__(self, name, age, email):

        self.name = name
        self.age = age
        self.email = email

    # --------------------------------------------------------
    # Instance Method
    # --------------------------------------------------------
    # An instance method works with the data of a particular
    # object. It uses self to access that object's properties.
    # --------------------------------------------------------

    def introduce(self):

        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"My email is {self.email}.")

    # --------------------------------------------------------
    # Class Method
    # --------------------------------------------------------
    # A class method works with class-level data.
    # cls represents the class itself, not an individual object.
    #
    # This method changes the university name for the class.
    # --------------------------------------------------------

    @classmethod
    def change_university(cls, new_name):

        cls.university = new_name

        print(f"University changed to: {cls.university}")

    # --------------------------------------------------------
    # Static Method
    # --------------------------------------------------------
    # A static method does not automatically receive self or cls.
    # It is used for a related utility operation.
    #
    # Here, we check whether a person is an adult.
    # --------------------------------------------------------

    @staticmethod
    def is_adult(age):

        return age >= 18

    # --------------------------------------------------------
    # Special Method: __str__
    # --------------------------------------------------------
    # Python automatically calls this method when print()
    # is used with a Person object.
    #
    # It returns a readable string representation.
    # --------------------------------------------------------

    def __str__(self):

        return f"Person: {self.name}, Age: {self.age}"

    # --------------------------------------------------------
    # Special Method: __repr__
    # --------------------------------------------------------
    # This method provides a developer-friendly representation.
    # It is especially useful when inspecting objects.
    # --------------------------------------------------------

    def __repr__(self):

        return f"Person(name='{self.name}', age={self.age})"


# ============================================================
# 2. STUDENT CLASS
# ============================================================
# Student inherits from Person.
#
# This means Student automatically receives the properties
# and methods defined in Person.
#
# Student also has additional properties and methods.
# ============================================================

class Student(Person):

    # Static property belonging to Student class.
    total_students = 0

    def __init__(self, name, age, email, student_id, major):

        # super() calls the constructor of the parent class.
        # This initializes name, age and email.
        super().__init__(name, age, email)

        # Additional Student properties.
        self.student_id = student_id
        self.major = major

        # Private property.
        # The double underscore makes direct access harder
        # through Python's name-mangling mechanism.
        self.__gpa = 0.0

        # Increase the number of created students.
        Student.total_students += 1

    # --------------------------------------------------------
    # Encapsulation: Getter
    # --------------------------------------------------------
    # This method provides controlled access to the private GPA.
    # --------------------------------------------------------

    def get_gpa(self):

        return self.__gpa

    # --------------------------------------------------------
    # Encapsulation: Setter
    # --------------------------------------------------------
    # This method validates the new GPA before changing it.
    # GPA must be between 0.0 and 4.0.
    # --------------------------------------------------------

    def set_gpa(self, new_gpa):

        if 0.0 <= new_gpa <= 4.0:

            self.__gpa = new_gpa

            print(f"GPA updated: {self.__gpa}")

        else:

            print("Invalid GPA! GPA must be between 0.0 and 4.0.")

    # --------------------------------------------------------
    # Student-specific instance method.
    # --------------------------------------------------------

    def study(self, subject):

        print(f"{self.name} is studying {subject}.")

    # --------------------------------------------------------
    # Method overriding.
    # --------------------------------------------------------
    # The Student class provides its own version of introduce().
    # It overrides the method inherited from Person.
    # --------------------------------------------------------

    def introduce(self):

        print(f"I am {self.name}, a student.")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")

    # Special method for readable Student representation.
    def __str__(self):

        return f"Student: {self.name} | ID: {self.student_id}"


# ============================================================
# 3. TEACHER CLASS
# ============================================================
# Teacher also inherits from Person.
#
# It shares common properties such as name, age and email.
# However, it has its own additional properties and methods.
# ============================================================

class Teacher(Person):

    total_teachers = 0

    def __init__(self, name, age, email, subject, salary):

        # Initialize inherited properties.
        super().__init__(name, age, email)

        # Teacher-specific properties.
        self.subject = subject
        self.salary = salary

        Teacher.total_teachers += 1

    # Teacher-specific method.
    def teach(self):

        print(f"{self.name} is teaching {self.subject}.")

    # Override the parent class method.
    def introduce(self):

        print(f"I am {self.name}, a university teacher.")
        print(f"Subject: {self.subject}")
        print(f"Salary: ${self.salary}")


# ============================================================
# 4. COURSE CLASS
# ============================================================
# This class represents a university course.
#
# Each Course object has its own name, teacher and student list.
# ============================================================

class Course:

    # Static property shared by all Course objects.
    university = "Global University"

    def __init__(self, course_name, teacher):

        self.course_name = course_name
        self.teacher = teacher

        # An empty list for storing enrolled students.
        self.students = []

    # --------------------------------------------------------
    # Enroll a student in the course.
    # --------------------------------------------------------

    def enroll_student(self, student):

        # Make sure the supplied object is a Student.
        if isinstance(student, Student):

            self.students.append(student)

            print(f"{student.name} enrolled in {self.course_name}.")

        else:

            print("Only Student objects can enroll.")

    # --------------------------------------------------------
    # Display all students enrolled in this course.
    # --------------------------------------------------------

    def show_students(self):

        print(f"\nStudents in {self.course_name}:")

        for student in self.students:

            print(f"- {student.name}")

    # --------------------------------------------------------
    # Display course information.
    # --------------------------------------------------------

    def show_course_info(self):

        print(f"Course: {self.course_name}")
        print(f"Teacher: {self.teacher.name}")
        print(f"University: {Course.university}")
        print(f"Number of students: {len(self.students)}")


# ============================================================
# 5. MAIN PROGRAM
# ============================================================
# In this section, we create objects and use their methods.
# ============================================================


print("\n========== UNIVERSITY MANAGEMENT SYSTEM ==========")


# ------------------------------------------------------------
# Create Student Objects
# ------------------------------------------------------------

student1 = Student(
    "Abdul",
    24,
    "abdul@example.com",
    "ST001",
    "Computer Engineering"
)

student2 = Student(
    "Ali",
    21,
    "ali@example.com",
    "ST002",
    "Software Engineering"
)


# ------------------------------------------------------------
# Create Teacher Object
# ------------------------------------------------------------

teacher1 = Teacher(
    "John",
    40,
    "john@example.com",
    "Python Programming",
    5000
)


# ============================================================
# 6. ORDINARY AND STATIC PROPERTIES
# ============================================================

print("\n========== PROPERTIES ==========")

# Ordinary properties belong to individual objects.
print("Student 1 name:", student1.name)
print("Student 2 name:", student2.name)

# Static properties belong to the class.
print("University:", Person.university)


# ============================================================
# 7. INSTANCE METHODS
# ============================================================

print("\n========== INSTANCE METHODS ==========")

# Each object executes its own method.
student1.study("Python")
student2.study("Java")

teacher1.teach()


# ============================================================
# 8. ENCAPSULATION
# ============================================================

print("\n========== ENCAPSULATION ==========")

# Update private GPA through the setter method.
student1.set_gpa(3.8)
student2.set_gpa(3.5)

# Read private GPA through the getter method.
print("Student 1 GPA:", student1.get_gpa())
print("Student 2 GPA:", student2.get_gpa())

# Try to assign an invalid GPA.
student1.set_gpa(5.0)


# ============================================================
# 9. CLASS METHODS
# ============================================================

print("\n========== CLASS METHODS ==========")

# Change the university name for the Person class.
Person.change_university("International University")

print("Current university:", Person.university)


# ============================================================
# 10. STATIC METHODS
# ============================================================

print("\n========== STATIC METHODS ==========")

# Check whether students are adults.
print("Is Abdul an adult?", Person.is_adult(student1.age))
print("Is Ali an adult?", Person.is_adult(student2.age))


# ============================================================
# 11. INHERITANCE AND POLYMORPHISM
# ============================================================

print("\n========== POLYMORPHISM ==========")

# Store different object types in one list.
people = [student1, student2, teacher1]

# The same method call produces different results.
# Python automatically selects the correct introduce() method
# depending on the actual object's class.
for person in people:

    person.introduce()

    print("------------------------")


# ============================================================
# 12. COURSE MANAGEMENT
# ============================================================

print("\n========== COURSE MANAGEMENT ==========")

# Create a course and assign a teacher.
python_course = Course("Python Programming", teacher1)

# Enroll students.
python_course.enroll_student(student1)
python_course.enroll_student(student2)

# Display course information.
python_course.show_course_info()

# Display enrolled students.
python_course.show_students()


# ============================================================
# 13. SPECIAL METHODS
# ============================================================

print("\n========== SPECIAL METHODS ==========")

# __str__ is automatically called by print().
print(student1)

# __repr__ returns a developer-friendly representation.
print(repr(student1))


# ============================================================
# 14. CLASS STATISTICS
# ============================================================

print("\n========== UNIVERSITY STATISTICS ==========")

# Display the number of created objects.
print("Total students:", Student.total_students)
print("Total teachers:", Teacher.total_teachers)

# ============================================================
# END OF PROGRAM
# ============================================================

print("\n========== PROGRAM FINISHED ==========")
