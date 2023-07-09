"""
Author: Alex Cox
Last date modified: 07/08/2023

Main - Standalone
"""
from student import Student
import unittest
import student_tests

def main():
    # Create two student objects
    student1 = Student('Appleseed', 'John', 'Computer Science', 3.5)
    student2 = Student('Haro', 'Anna', 'Biology', 1.8)

    # Print the student objects
    print(student1)
    print(student2)

    # Ask the user if they want to run the tests
    run_tests = input("Do you want to run the unit tests? (y/n) ")
    if run_tests.lower() == 'y':
        suite = unittest.TestLoader().loadTestsFromModule(student_tests)
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    # Run the main function 
    main()
