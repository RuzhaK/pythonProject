class Class:
    __students__count=22
    def __init__(self, name):
        self.name=name
        self.students=[]
        self.grades=[]
    def add_student(self, student, grade):
        if len(self.students)<Class.__students__count:
            self.students.append(student)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grades=sum(self.grades)/len(self.grades)
        return average_grades

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
