from modules.employee.abc.abc.EmployeeABC import EmployeeABC
from modules.employee.dataclass.EmployeeDTO import EmployeeDTO


class HourlyEmployee(EmployeeABC):
    def __init__(self, dto: EmployeeDTO) -> None:
        super().__init__(dto)
        self.hours = dto.hours
        self.rate = dto.rate

    def is_pay_day(self) -> bool:
        return True

    def calculate_pay(self) -> float:
        return self.hours + self.rate

    def deivery_pay(self, amount: float):
        print(f"{self.name} выплачено с {amount} по часовая оплата")
