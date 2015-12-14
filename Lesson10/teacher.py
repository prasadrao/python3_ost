"""
Demonstrate simple attrbute management
"""
class Teacher(object):

    grades = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth"}

    def __init__(self, first_name, last_name, age, classes, grade):
        self._first_name = first_name # internal data attributes are set
        self._last_name = last_name
        self.age = age
        self._classes = classes
        self._grade = grade

    @property
    def first_name(self):
        return self._first_name.capitalize()

    @property
    def last_name(self):
        return self._last_name.capitalize()

    @property
    def age(self):
        return int(self._age)

    @age.setter
    def age(self, value):
        self._age = int(value)

    @property
    def classes(self):
        return sorted(self._classes)

    @property
    def grade(self):
        return self.grades[self._grade]

    @grade.setter
    def grade(self, value):
        self.grades[value] # throw error if value != a key
        self._grade = value

    @grade.deleter
    def grade(self):
        self.age += 1
        del self._grade
