# تعريف الكلاسات قبل استخدامها

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

# تعريف الكلاسات الإضافية

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')

class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')

# إنشاء موظفين ونظام الرواتب

salary_employee = SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)

# نظام الرواتب
class PayrollSystem:
    def calculate_payroll(self, employees):
        for employee in employees:
            print(f'Payroll for: {employee.name} - Check amount: {employee.calculate_payroll()}')

payroll_system = PayrollSystem()
payroll_system.calculate_payroll([salary_employee, hourly_employee, commission_employee])

# إنشاء موظفين إضافيين ونظام الإنتاجية

manager = Manager(4, 'Mary Poppins', 3000)
secretary = Secretary(5, 'John Smith', 1500)
sales_guy = SalesPerson(6, 'Kevin Bacon', 1000, 250)
factory_worker = FactoryWorker(7, 'Jane Doe', 40, 15)

employees = [manager, secretary, sales_guy, factory_worker]

# نظام الإنتاجية
class ProductivitySystem:
    def track(self, employees, hours):
        for employee in employees:
            employee.work(hours)

productivity_system = ProductivitySystem()
productivity_system.track(employees, 40)

# نظام الرواتب مرة أخرى
payroll_system.calculate_payroll(employees)
