from dataclasses import dataclass

from modules.employee.enum.EmployeeEnum import EmployeeEnum


@dataclass
class EmployeeDTO:
    name: str
    type: EmployeeEnum
    salary: float = 0
    base: float = 0
    commission: float = 0
    hours: float = 0
    rate: float = 0
