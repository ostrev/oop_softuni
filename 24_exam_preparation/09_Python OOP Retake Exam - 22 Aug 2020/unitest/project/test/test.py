from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard('student', 4)

            

if __name__ == '__main__':
    main()
