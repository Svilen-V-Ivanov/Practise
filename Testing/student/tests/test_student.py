from student.project.student import Student
from unittest import TestCase, main


class StudentTesting(TestCase):
    NAME = 'John'
    COURSE_NAME = 'Math'
    COURSE_NOTE = [3]

    def setUp(self) -> None:
        self.student = Student(self.NAME)

    def test__when_valid_credentials_without_courses__creates_instance_correctly(self):
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test__when_valid_credentials_with_none_courses__creates_instance_correctly(self):
        courses = None
        student = Student(self.NAME, courses)
        self.assertEqual(self.NAME, student.name)
        self.assertEqual({}, student.courses)

    def test__when_valid_credentials_with_courses__creates_instance_correctly(self):
        courses = {'a': [1], 'b': [2]}
        student = Student(self.NAME, courses)
        self.assertEqual(self.NAME, student.name)
        self.assertEqual(courses, student.courses)

    def test__when_enrolling_and_course_already_exists__return_correct_message(self):
        courses = {self.COURSE_NAME: self.COURSE_NOTE}
        student = Student(self.NAME, courses)
        notes = [1, 2, 3]
        course_notes = 'Y'
        expected_notes = self.COURSE_NOTE + notes
        actual_result = student.enroll(self.COURSE_NAME, notes, course_notes)
        expected_result = "Course already added. Notes have been updated."

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_notes, courses[self.COURSE_NAME])

    def test__when_enrolling_course_not_in_dict_and_add_course_notes_is_blank__perform_correct_action(self):
        courses = {'a': [1], 'b': [2]}
        student = Student(self.NAME, courses)
        notes = [1, 2, 3]
        course_notes = ''
        expected_courses = {'a': [1], 'b': [2], self.COURSE_NAME: notes}
        actual_result = student.enroll(self.COURSE_NAME, notes, course_notes)
        expected_result = "Course and course notes have been added."

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, student.courses)

    def test__when_enrolling_course_not_in_dict_and_add_course_notes_is_y__perform_correct_action(self):
        courses = {'a': [1], 'b': [2]}
        student = Student(self.NAME, courses)
        notes = [1, 2, 3]
        course_notes = 'Y'
        expected_courses = {'a': [1], 'b': [2], self.COURSE_NAME: notes}
        actual_result = student.enroll(self.COURSE_NAME, notes, course_notes)
        expected_result = "Course and course notes have been added."

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, student.courses)

    def test__when_enrolling_course_not_in_dict_and_add_course_notes_is_not_blank_or_y__perform_correct_action(self):
        courses = {'a': [1], 'b': [2]}
        student = Student(self.NAME, courses)
        notes = [1, 2, 3]
        course_notes = 'T'
        expected_courses = {'a': [1], 'b': [2], self.COURSE_NAME: []}
        actual_result = student.enroll(self.COURSE_NAME, notes, course_notes)
        expected_result = "Course has been added."

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, student.courses)

    def test__when_add_notes_and_course_not_in_dict__raise_correct_exception(self):
        courses = {'a': [1], 'b': [2]}
        notes = [4]
        student = Student(self.NAME, courses)
        expected_result = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as error:
            student.add_notes(self.COURSE_NAME, notes)
        self.assertEqual(expected_result, str(error.exception))
        self.assertEqual(courses, student.courses)

    def test__when_add_notes_and_course_in_dict__perform_correct_action(self):
        courses = {'a': [1], 'b': [2], self.COURSE_NAME: self.COURSE_NOTE}
        notes = [4]
        student = Student(self.NAME, courses)
        expected_result = "Notes have been updated"
        expected_notes = {'a': [1], 'b': [2], self.COURSE_NAME: [3, notes]}
        actual_result = student.add_notes(self.COURSE_NAME, notes)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_notes, student.courses)

    def test__when_leaving_course_and_course_not_in_dict__raise_correct_exception(self):
        courses = {'a': [1], 'b': [2]}
        student = Student(self.NAME, courses)
        expected_result = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as error:
            student.leave_course(self.COURSE_NAME)
        self.assertEqual(expected_result, str(error.exception))
        self.assertEqual(courses, student.courses)

    def test__when_leaving_course_and_name_in_dict__perform_correct_operations(self):
        courses = {'a': [1], 'b': [2], self.COURSE_NAME: self.COURSE_NOTE}
        student = Student(self.NAME, courses)
        expected_result = "Course has been removed"
        expected_courses = {'a': [1], 'b': [2]}
        actual_result = student.leave_course(self.COURSE_NAME)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, student.courses)

    if __name__ == '__main__':
        main()