from unittest import TestCase, main
from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student('Gosho', None)

    def test_init_empty_courses(self):
        self.assertEqual('Gosho', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init(self):
        self.student.courses['course_one'] = ['note_1', 'note_2']
        self.assertEqual('Gosho', self.student.name)
        self.assertEqual({'course_one': ['note_1', 'note_2']}, self.student.courses)

    def test_enroll_course_is_add_update_notes(self):
        self.student.courses['course_one'] = ['note_1', 'note_2']
        self.assertEqual("Course already added. Notes have been updated.", self.student.enroll('course_one', ['note_3', 'note_4'], 'Y' ))
        self.assertEqual({'course_one': ['note_1', 'note_2', 'note_3', 'note_4']}, self.student.courses)

    def test_enroll_course_and_notes_add_Y(self):
        self.assertEqual("Course and course notes have been added.",
                         self.student.enroll('course_one', ['note_3', 'note_4'], 'Y'))
        self.assertEqual({'course_one': ['note_3', 'note_4']}, self.student.courses)

    def test_enroll_course_and_notes_add_no_string(self):
        self.assertEqual("Course and course notes have been added.",
                         self.student.enroll('course_one', ['note_3', 'note_4'], ''))
        self.assertEqual({'course_one': ['note_3', 'note_4']}, self.student.courses)

    def test_enroll_add_course(self):
        self.assertEqual("Course has been added.", self.student.enroll('course_one', ['note_3', 'note_4'], 'add'))
        self.assertEqual({'course_one': []}, self.student.courses)

    def test_add_notes(self):
        self.student.courses['course_one'] = []
        self.assertEqual("Notes have been updated", self.student.add_notes('course_one', 'note_5'))
        self.assertEqual({'course_one': ['note_5']}, self.student.courses)

    def test_add_notes_raise_name_not_in(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('course_one', 'note_5')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        self.student.courses['course_one'] = []
        self.assertEqual("Course has been removed", self.student.leave_course('course_one'))
        self.assertEqual({}, self.student.courses)

    def test_leave_course_raise_name_not_in(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('course_one')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == '__main__':
    main()
