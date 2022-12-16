from project.helpers.validator import Validate
from project.table.inside_table import InsideTable
from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validate.validate_outside_table(value, "Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value


# out_table = OutsideTable(55, 4)
# in_table = InsideTable(5, 4)
#
# print(out_table.free_table_info())
# print(in_table.free_table_info())
#
# a= 1
