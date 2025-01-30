# Employee Management System 
class Employee:
    def __init__(self,  emp_id, name, deptt, salary):
        self.emp_id = emp_id
        self.name = name
        self.deptt = deptt
        self.salary = salary
    def get_details(self):
        return f'''Employee Id: {self.emp_id}
Name: {self.name}
Department: {self.deptt}
Salary: {self.salary}'''

    def update_details(self, name=None, deptt=None, salary=None):
        if name:
            self.name = name
        if deptt:
            self.deptt = deptt
        if salary:
            self.salary = salary
    def increment_salary(self, prec):
        self.salary += (prec/100 * salary)




class Employee_Management:
    def __init__(self):
        print('Management tools initialized \nSystem Ready\n\n')
        self.reg = {}

    def add_employee(self, emp_id, name, deptt, salary):
        self.reg[emp_id] = Employee(emp_id, name, deptt, salary) 
    
    def display_all_employee(self):
        count = 1
        for key in self.reg:
            print(f'\nEmployee {count}: Details')
            print(self.reg[key].get_details())
            count += 1

    

system = Employee_Management()
while 1:
    # main code 
    print('Welcome to GLA University\n\n')

    print('Available Choice\n')
    print('''
    1. Add Employee
    2. Update Employee Info
    3. Display All Employees
    4. Delete Employee by ID 
    5. Salary Increment by ID
    6. Exit
    ''')
    choice = int(input('Enter the choice [1-6]'))
    if choice == 1:
        e_id = input('Enter the Employee ID')
        name = input('Enter the Employee Name')
        dept = input('Enter the Employee Department')
        salary = int(input('Enter the Salary '))

        system.add_employee(e_id, name, dept, salary)
    elif choice == 3:
        system.display_all_employee()






