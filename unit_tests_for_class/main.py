"""
Unit Tests for a Class Assignment
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

   # Prompt user to run unit tests
    run_tests = input("Do you want to run unit tests? (yes/no): ")
    while run_tests.lower() not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        run_tests = input("Do you want to run unit tests? (yes/no): ")
    if run_tests.lower() == 'yes':
        try:
            suite = unittest.TestLoader().loadTestsFromModule(student_tests)
            unittest.TextTestRunner().run(suite)
        except Exception as e:
            print(f"An error occurred while running the tests: {e}")
    
    del student1
    del student2

if __name__ == '__main__':
    # Run the main function 
    main()
