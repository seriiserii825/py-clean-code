from modules.employee.abc.abc.EmployeeABC import EmployeeABC
from modules.employee.dataclass.EmployeeDTO import EmployeeDTO


class SalariedEmployee(EmployeeABC):
    def __init__(self, dto: EmployeeDTO) -> None:
        super().__init__(dto)
        self.salary = dto.salary

    def is_pay_day(self) -> bool:
        return True

    def calculate_pay(self) -> float:
        return self.salary

    def deivery_pay(self, amount: float):
        print(f"{self.name} выплачено с {amount} фиксированная зарплата")
