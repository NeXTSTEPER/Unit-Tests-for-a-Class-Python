"""
Author: Alex Cox
Last date modified: 07/08/2023

All in One File Implementation

Basic Student class with some simple attributes like first and last name, major, and GPA.

StudentTests is the unit tests class which tests the Student test

As Well as the Main

"""
import unittest

class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError("Names can only include alphabetic characters, hyphen, and apostrophe")
        if not major:
            raise ValueError("Major is required")
        if not lname or not name_characters.issuperset(lname):
            raise ValueError("Valid last name is required")
        if not fname or not name_characters.issuperset(fname):
            raise ValueError("Valid first name is required")
        if not isinstance(gpa, float) or gpa < 0.0 or gpa > 4.0:
            raise ValueError("GPA must be a float between 0.0 and 4.0")

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)



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

def main():
    # Create two student objects
    student1 = Student('Appleseed', 'John', 'Computer Science', 3.5)
    student2 = Student('Haro', 'Anna', 'Biology', 1.8)

    # Print the student objects
    print(student1)
    print(student2)
    
#Driver code
if __name__ == '__main__':
    # Run the main function if the script is run directly
    main()

    # Run all the tests when the script is executed
    unittest.main()
