from project.helpers.validator import Validate
from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validate.validate_inside_table(value, "Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value
