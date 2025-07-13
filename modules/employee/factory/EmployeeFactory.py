from modules.employee.abc.abc.EmployeeABC import EmployeeABC
from modules.employee.concrete.CommisionedEmployee import CommisionedEmployee
from modules.employee.concrete.HourlyEmployee import HourlyEmployee
from modules.employee.concrete.SalariedEmployee import SalariedEmployee
from modules.employee.dataclass.EmployeeDTO import EmployeeDTO
from modules.employee.enum.EmployeeEnum import EmployeeEnum
from modules.employee.exception.InvalidEmployeeType import InvalidEmployeeType


class EmployeeFactory:
    @staticmethod
    def make_employee(dto: EmployeeDTO) -> EmployeeABC:
        match dto.type:
            case EmployeeEnum.COMMISIONED:
                return CommisionedEmployee(dto)
            case EmployeeEnum.HOURLY:
                return HourlyEmployee(dto)
            case EmployeeEnum.SALARIED:
                return SalariedEmployee(dto)
            case _:
                raise InvalidEmployeeType(f"неверный тип: {dto.type}")
