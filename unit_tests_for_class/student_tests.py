"""
Author: Alex Cox
Last date modified: 07/08/2023


StudentTests is the unit tests class which tests the Student test

"""
import unittest
from student import Student

#test class - contains test classes as name suggests
class StudentTests(unittest.TestCase):

    def setUp(self):
        # This method is used for setup actions
        # Creating two instances of the Student class
        self.student1 = Student('Appleseed', 'John', 'Computer Science', 3.5)
        self.student2 = Student('Haro', 'Anna', 'Biology', 1.8)

    def tearDown(self):
        # This method is used for cleanup actions
        del self.student1
        del self.student2


    def test_object_created_required_attributes(self):
        # Test that the constructor sets the required attributes correctly
        self.assertEqual(self.student1.last_name, 'Appleseed')
        self.assertEqual(self.student1.first_name, 'John')
        self.assertEqual(self.student1.major, 'Computer Science')
        self.assertEqual(self.student1.gpa, 3.5)

        self.assertEqual(self.student2.last_name, 'Haro')
        self.assertEqual(self.student2.first_name, 'Anna')
        self.assertEqual(self.student2.major, 'Biology')
        self.assertEqual(self.student2.gpa, 1.8)

    def test_object_created_all_attributes(self):
        # Test that the constructor sets all attributes correctly
        self.assertEqual(self.student1.last_name, 'Appleseed')
        self.assertEqual(self.student1.first_name, 'John')
        self.assertEqual(self.student1.major, 'Computer Science')
        self.assertEqual(self.student1.gpa, 3.5)

    def test_student_str(self):
        # Test the string representation of the Student class
        self.assertEqual(str(self.student1), 'Appleseed, John has major Computer Science with gpa: 3.5')
        self.assertEqual(str(self.student2), 'Haro, Anna has major Biology with gpa: 1.8')

    def test_object_not_created_error_last_name(self):
        # Test that an exception is raised when the last name is not provided
        with self.assertRaises(ValueError):
            s = Student('', 'John', 'Computer Science', 3.5)

    def test_object_not_created_error_first_name(self):
        # Test that an exception is raised when the first name is not provided
        with self.assertRaises(ValueError):
            s = Student('Appleseed', '', 'Computer Science', 3.5)

    def test_object_not_created_error_major(self):
        # Test that an exception is raised when the major is not provided
        with self.assertRaises(ValueError):
            s = Student('Appleseed', 'John', '', 3.5)

    def test_object_not_created_error_gpa(self):
        # Test that an exception is raised when the GPA is not a float or not in the valid range
        with self.assertRaises(ValueError):
            s = Student('Appleseed', 'John', 'Computer Science', '3.5')
        with self.assertRaises(ValueError):
            s = Student('Appleseed', 'John', 'Computer Science', 4.5)
        with self.assertRaises(ValueError):
            s = Student('Appleseed', 'John', 'Computer Science', -1.0)
            
if __name__ == '__main__':
    # Run all the tests when the script is executed
    unittest.main()
