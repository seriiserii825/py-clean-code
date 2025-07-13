from modules.employee.abc.abc.EmployeeABC import EmployeeABC
from modules.employee.dataclass.EmployeeDTO import EmployeeDTO


class CommisionedEmployee(EmployeeABC):
    def __init__(self, dto: EmployeeDTO) -> None:
        super().__init__(dto)
        self.base = dto.base
        self.commission = dto.commission

    def is_pay_day(self) -> bool:
        return True

    def calculate_pay(self) -> float:
        return self.base + self.commission

    def deivery_pay(self, amount: float):
        print(f"{self.name} выплачено с {amount} комиссией")
