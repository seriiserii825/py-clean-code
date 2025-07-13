from modules.employee.dataclass.EmployeeDTO import EmployeeDTO
from modules.employee.enum.EmployeeEnum import EmployeeEnum
from modules.employee.factory.EmployeeFactory import EmployeeFactory

employees = [
    EmployeeDTO(name="Serii", type=EmployeeEnum.COMMISIONED, salary=1500),
    EmployeeDTO(name="Alina", type=EmployeeEnum.HOURLY, hours=4, rate=10),
    EmployeeDTO(name="Stepan", type=EmployeeEnum.SALARIED, salary=14200),
]

for dto in employees:
    employee = EmployeeFactory.make_employee(dto)
    if employee.is_pay_day():
        pay = employee.calculate_pay()
        employee.deivery_pay(pay)
