class Employee:
    def __init__(self, name, salary, location):
        self.__name = name
        self.__salary = salary
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
        return print(f"Employee name:{self.employee_id}\nbase salary: {self.__salary}\nlocation: {self.__location}\n")

    @staticmethod
    def bonus():
        """when invoked it will give a bonus of 5k and don't forget to add it to total pay"""
        bonus = 1000 * 10 * 0.5
        return bonus

    def get_total_pay(self, work_time, ext_bonus=0):
        """calculation of salary"""
        total_pay = 0
        if 220 > work_time >= 180:
            total_pay = self.__salary
        elif work_time > 220:
            total_pay = self.__salary * 1.2
            if ext_bonus > 0:
                total_pay += ext_bonus
        elif work_time < 180:
            total_pay = self.__salary * 0.8

        return total_pay


# todo-2:getter and setters for the member variables
# todo-3: specify method "get_total_pay()" in the base class which is overridden in both the fulltime and contract

class FulltimeEmployee(Employee):
    def __init__(self, department, name="null", salary=10000, location="USA"):
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
    #
    # def get_total_pay(self, work_time):
    #     total_pay = self.salary
    #     if 220 > work_time >= 180:
    #         total_pay = self.__salary
    #     elif work_time > 220:
    #         total_pay *= 1.2
    #     elif work_time < 180:
    #         total_pay *= 0.8
    #     return print(total_pay)


class ContractWorker(Employee):
    def __init__(self, division, name="null", salary=10000):
        Employee.__init__(self, division, salary=salary, location="USA")
        self.name = name.capitalize()
        self.salary = salary
        self.division = division

    def set_raise(self, num):
        self.salary += num

    def get_info(self):
        return print(f"Employee name:{self.name}\ndivision: {self.division}\nbase salary: {self.salary}\nlocation: "
                     f"{Employee.get_location(self)}")

    # def get_total_pay(self, work_time):
    #     total_pay = self.salary
    #     if 220 > work_time >= 180:
    #         total_pay = self.salary
    #     elif work_time < 150:
    #         total_pay = "you are fired!!"
    #     elif work_time < 180:
    #         total_pay *= 0.8
    #     return print(total_pay)
