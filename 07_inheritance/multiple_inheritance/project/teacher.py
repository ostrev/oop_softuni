from project.employee import Employee
from project.reptile import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'
