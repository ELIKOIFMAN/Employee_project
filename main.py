class Employee:
    def __init__(self, name, salary, location):
        self.__name = name
        self.salary = salary
        self.__location = location

    def __repr__(self):
        return '{}'.format(self.__name)

    @property
    def employee_id(self):
        """get info about employee"""
        return self.__name

    @employee_id.setter
    def employee_id(self, new_name):
        """set new ID for the employee"""
        self.__name = new_name

    @employee_id.deleter
    def employee_id(self):
        """delete the employee"""
        del self

    def get_info(self):
        """get all the info about a certain employee"""
        return print(f"Employee name:{self.employee_id}\nbase salary: {self.salary}\nlocation: {self.__location}\n")

    @staticmethod
    def bonus():
        """when invoked it will give a bonus of 5k and don't forget to add it to total pay"""
        bonus = 1000 * 10 * 0.5
        return bonus

    def get_salary(self):
        return self.salary

    def get_total_pay(self, work_time, ext_bonus=0):
        """calculation of salary"""
        total_pay = 0
        if ext_bonus > 0:
            total_pay += ext_bonus
        if 220 > work_time >= 180:
            total_pay = self.salary
        elif work_time > 220:
            total_pay = self.salary * 1.2
        elif work_time < 180:
            total_pay = self.salary * 0.8

        return total_pay

    def salary_after_tax(self, payment=0):
        """payment calculation after tax"""
        tax = 0
        if payment > 6790:
            # first pay grade
            tax = 6790 * 0.1
            if payment >= 9730:
                # we passed the 2nd pay grade
                pay_grade = 9730 - 6791
                tax = tax + (pay_grade * 0.14)
                if payment > 15620:
                    #  we passed the 3rd pay grade
                    pay_grade = 15620 - 9731
                    tax = tax + (pay_grade * 0.2)
                    if payment > 21710:
                        # we passed the 4th pay grade
                        pay_grade = 21710 - 15621
                        tax = tax + (pay_grade * 0.31)
                        if payment > 45180:
                            # we passed the 5th pay grade
                            pay_grade = 45180 - 21711
                            tax = tax + (pay_grade * 0.35)
                            if payment > 58191:
                                # 7th pay grade
                                pay_grade = (payment - 58191) * 0.5
                                tax = tax + pay_grade
                            elif payment <= 58190:
                                # 6th pay grade
                                pay_grade = (payment - 45181) * 0.47
                                tax = tax + pay_grade
                        elif payment <= 45180:
                            # 5th pay grade
                            pay_grade = payment - 21711
                            tax = tax + (pay_grade * 0.35)
                    elif payment <= 21710:
                        # 4th pay grade
                        pay_grade = payment - 15621
                        tax = tax + (pay_grade * 0.31)
                elif payment <= 15620:
                    # 3rd pay grade
                    pay_grade = payment - 9731
                    tax = tax + (pay_grade * 0.2)
            elif payment > 6790:
                # 2nd pay grade
                pay_grade = payment - 6791
                tax = tax + (pay_grade * 0.14)
        elif payment <= 6790:
            tax = payment * 0.1
        after_tax = payment - tax
        return print(f"you salary after tax is:{after_tax}")


# todo-2:getter and setters for the member variables
# todo-3: specify method "get_total_pay()" in the base class which is overridden in both the fulltime and contract

class FulltimeEmployee(Employee):
    def __init__(self, department, name="null", salary=10000, location="Israel"):
        Employee.__init__(self, department, name, salary)
        self.name = name.capitalize()
        self.salary = salary
        self.department = department
        self.location = location

    # def set_raise(self, num):
    #     self.salary += num
    #
    def get_info(self):
        return print(f"Employee name:{self.name}\nbase salary: {self.salary}\nlocation: {self.location}\ndivision: "
                     f"{self.department}\n")


class ContractWorker(Employee):
    def __init__(self, department, name="null", salary=10000, location="Israel"):
        Employee.__init__(self, department, name, salary)
        self.name = name.capitalize()
        self.salary = salary
        self.division = department
        self.location = location

    def set_raise(self, num):
        self.salary += num

    def get_info(self):
        return print(f"Employee name:{self.name}\ndivision: {self.division}\nbase salary: {self.salary}\nlocation: "
                     f"{self.location}")

    # def get_total_pay(self, work_time):
    #     total_pay = self.salary
    #     if 220 > work_time >= 180:
    #         total_pay = self.salary
    #     elif work_time < 150:
    #         total_pay = "you are fired!!"
    #     elif work_time < 180:
    #         total_pay *= 0.8
    #     return print(total_pay)
