class Student:
    def __init__ (self, name, id, age, grade):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade

# creating instances of Student

student1 = Student("Will", "AF90DGH", 17, "A-")
student2 = Student("Pat", "PH945SD", 18, "A")

#Print attributes of student1
print("Attributes of student1:")
print("Name:", student1.name)
print("Student ID:", student1.id)
print("Age:", student1.age)
print("Grade:", student1.grade)

#Print attributes of student2
print("Attributes of student2:")
print("Name:", student2.name)
print("Student ID:", student2.id)
print("Age:", student2.age)
print("Grade:", student2.grade)