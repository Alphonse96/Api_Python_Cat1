# EMPLOYEE AND DEPARTMENT MANAGEMENT SYSTEM

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Displays the employee's details."""
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary:.2f}")

    def update_salary(self, new_salary):
        """Updates the employee's salary."""
        self.salary = new_salary
        print(f"Salary for {self.name} updated to ${self.salary:.2f}.")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to hold Employee objects

    def add_employee(self, employee):
        """Adds an employee to the department."""
        self.employees.append(employee)
        print(f"{employee.name} has been added to the {self.department_name} department.")

    def calculate_total_salary(self):
        """Calculates and displays the total salary expenditure for the department."""
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"\nTotal salary expenditure for the {self.department_name} department: ${total_salary:.2f}")
        return total_salary

    def display_all_employees(self):
        """Displays all employees in the department."""
        if self.employees:
            print(f"\nEmployees in the {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in the {self.department_name} department yet.")

# Interactive code to manage employees and departments
def main():
    # Creating a department
    department_name = input("Enter department name: ")
    department = Department(department_name)

    while True:
        print("\nEmployee and Department Management System")
        print("1. Add Employee")
        print("2. Update Employee Salary")
        print("3. Display All Employees")
        print("4. Calculate Total Salary Expenditure")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            salary = float(input("Enter employee salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            if not department.employees:
                print("No employees in the department yet.")
            else:
                print("\nSelect an employee to update salary:")
                for i, employee in enumerate(department.employees, 1):
                    print(f"{i}. {employee.name}")
                employee_choice = int(input(f"Select an employee (1-{len(department.employees)}): ")) - 1
                employee = department.employees[employee_choice]

                new_salary = float(input(f"Enter the new salary for {employee.name}: "))
                employee.update_salary(new_salary)

        elif choice == "3":
            department.display_all_employees()

        elif choice == "4":
            department.calculate_total_salary()

        elif choice == "5":
            print("Exiting the Employee and Department Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
