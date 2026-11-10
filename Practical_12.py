
class Employee:

    count = 0

    def __init__(self, emp_no, name, dept, basic, da, hra):

        if basic < 0 or da < 0 or hra < 0:
            raise ValueError("Salary cannot be negative")

        self.emp_no = emp_no
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra

        Employee.count += 1

    def salary(self):
        return self.basic + self.da + self.hra

    def __del__(self):
        Employee.count -= 1

    def __str__(self):
        return (
            "Employee Number: " + str(self.emp_no) +
            "\nName: " + self.name +
            "\nDepartment: " + self.dept +
            "\nBasic Salary: " + str(self.basic) +
            "\nDA: " + str(self.da) +
            "\nHRA: " + str(self.hra) +
            "\nTotal Salary: " + str(self.salary())
        )


# Creating employee objects

e1 = Employee(101, "Rahul", "IT", 20000, 5000, 3000)

e2 = Employee(102, "Aman", "HR", 25000, 6000, 4000)

print(e1)
print()
print(e2)

print("\nTotal Employees:", Employee.count)

del e1

print("Employees after deleting e1:", Employee.count)
