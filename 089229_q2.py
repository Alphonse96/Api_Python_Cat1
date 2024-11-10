# ONLINE COURSE MANAGEMENT SYSTEM

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Dictionary to store assignment names and grades

    def add_assignment(self, assignment_name, grade):
        """Adds an assignment and grade to the student's record."""
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' added with grade {grade} for {self.name}.")

    def display_grades(self):
        """Displays all grades for the student."""
        if self.assignments:
            print(f"\nGrades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f" - {assignment}: {grade}")
        else:
            print(f"{self.name} has no assignments yet.")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # List to hold Student objects

    def add_student(self, student):
        """Adds a student to the course."""
        self.students.append(student)
        print(f"{student.name} has been added to the course '{self.course_name}'.")

    def assign_grade(self, student, assignment_name, grade):
        """Assigns a grade to a student's assignment."""
        student.add_assignment(assignment_name, grade)

    def display_all_students_grades(self):
        """Displays all students and their grades."""
        if self.students:
            print(f"\nStudents enrolled in {self.course_name}:")
            for student in self.students:
                student.display_grades()
        else:
            print(f"No students enrolled in {self.course_name} yet.")

# Interactive code to manage students, assignments, and grades
def main():
    # Sample instructor
    instructor = Instructor("Dr. Smith", "Python Programming 101")

    while True:
        print("\nOnline Course Management System")
        print("1. Add a Student")
        print("2. Assign a Grade to a Student")
        print("3. Display All Students and Their Grades")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            if not instructor.students:
                print("No students are enrolled in the course yet.")
            else:
                print("\nSelect a student to assign a grade to:")
                for i, student in enumerate(instructor.students, 1):
                    print(f"{i}. {student.name}")
                student_choice = int(input("Select a student (1-{}): ".format(len(instructor.students)))) - 1
                student = instructor.students[student_choice]

                assignment_name = input("Enter assignment name: ")
                grade = input(f"Enter grade for '{assignment_name}': ")
                instructor.assign_grade(student, assignment_name, grade)

        elif choice == "3":
            instructor.display_all_students_grades()

        elif choice == "4":
            print("Exiting the Online Course Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
