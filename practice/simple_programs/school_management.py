class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name} \t Age: {self.age} \t Grade: {self.grade}")



class StudentManager:
    def __init__(self):
        self.students = []   

    def add_student(self, student):
        self.students.append(student)

    def show_all_students(self):
        for student in self.students:
            student.display_info()

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def update_student(self, name, new_grade):
        student = self.find_student(name)
        if student:
            student.grade = new_grade
            print("grade changed successfully!")
        else:
            print("student not found!")


def main():
    manager = StudentManager()

    s1 = Student("Max", 22, "O")
    s2 = Student("Shelly", 23, "C")
    s3 = Student("Colt", 15, "B")
    s4 = Student("Brock", 20, "A")

    manager.add_student(s1)
    manager.add_student(s2) 
    manager.add_student(s3) 
    manager.add_student(s4) 

    manager.show_all_students()
    manager.update_student("Colt", "A+")

    s3.display_info()

    manager.update_student("Tara", "F")



if __name__ == "__main__":
    main()