# Employee Management System 

class Employee:
    def __init__(self, name, emp_id, deptt, salary):
        self.name = name
        self.emp_id = emp_id
        self.deptt = deptt
        self.salary = salary
    def display_info(self):
        st = f'''Name: {self.name}
Employee Id: {self.emp_id}
Department: {self.deptt}
Salary: {self.salary}'''
        print(st)
    def update_info(self, name=None, deptt=None, salary=None):
        if name:
            self.name = name
        if deptt:
            self.deptt = deptt
        if salary:
            self.salary = salary
    def increment_salary(self,perc):
        self.salary += (perc/100) *self.salary


class Employee_management:
    def __init__(self):
        self.reg = {}
    def add_employee(self, name, emp_id, deptt, salary):
        if emp_id in self.reg:
            print('Employee id already exist')
        else:
            self.reg[emp_id] = Employee(name, emp_id, deptt, salary)
            print(f'Employee Id {emp_id} successfully created')
    def display_all_employee(self):
        for emp in self.reg:
            self.reg[emp].display_info()

# Main Code
systm = Employee_management()
systm.add_employee('Ravi', 'gla11763', 'cse', 10000)
systm.add_employee('Saket', 'gla18863', 'ece', 1000)
