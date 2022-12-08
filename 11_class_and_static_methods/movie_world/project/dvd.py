from project.month_convert import month_converter


class DVD:
    def __init__(self, name, id, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split('.')
        month_str = month_converter(int(month))
        return cls(name, id, int(year), month_str, age_restriction)

    def __repr__(self):
        rented = 'not rented'
        if self.is_rented:
            rented = 'rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented}"

