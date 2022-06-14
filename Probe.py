class Employee:
    name = 'Tom'
    salary = 10000

    def __int__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self):
        print(
            'Name: {} \nSalary: {}'.format(self.name, self.salary)
        )


emp_1 = Employee()
emp_1.print_info()
emp_2 = Employee()
emp_2.name = 'Bob'
emp_2.salary = 20000
emp_2.print_info()