"""
Author: Alex Cox
Last date modified: 07/08/2023

Basic Student class with same simple attributes like first and last name, major, and GPA.

"""

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

   
