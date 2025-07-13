from abc import ABC, abstractmethod

from modules.employee.dataclass.EmployeeDTO import EmployeeDTO


class EmployeeABC(ABC):
    def __init__(self, dto: EmployeeDTO) -> None:
        self.name = dto.name

    @abstractmethod
    def is_pay_day(self) -> bool:
        pass

    @abstractmethod
    def calculate_pay(self) -> float:
        pass

    @abstractmethod
    def deivery_pay(self, amount: float):
        pass
