class Student:
    def __init__(self, name, age, roll_number):
        self.__name = name
        self.__age = age
        self.__roll_number = roll_number

    # Get func -> To get the name age and roll number from the user
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_roll_number(self):
        return self.__roll_number

    # Set func -> To set the name age and roll number from the user
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    def display_info(self):
        print(f"Name: {self.get_name()}, Age: {self.get_age()}, Roll Number: {self.get_roll_number()}")

    def update_info(self, name = None, age = None, roll_number = None):
        if name:
            self.set_name(name)
        if age:
            self.set_age(age)
        if roll_number:
            self.set_roll_number(roll_number)


student1 = Student("Rick", 20, 101)
student1.display_info()
student1.update_info(name = "SD", age = 21, roll_number = 34)
student1.display_info()