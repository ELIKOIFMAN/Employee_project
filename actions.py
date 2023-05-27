from main import Employee,FulltimeEmployee
worker2 = Employee("eli",15000,"haifa")
# repr(worker2)
worker3 = FulltimeEmployee("R&D", "Sanjin", 50000)
worker2.name = "Eli"
worker2.bonus()
worker2.get_info()
worker3.get_info()
worker3.get_total_pay(230)
worker3.get_info()
