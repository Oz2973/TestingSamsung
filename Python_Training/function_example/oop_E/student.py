from Python_Training import person


class student(person):

    def average_calc(self,grades):
        summary = 0
        for grade in grades:
            summary = summary + grade

            grades_size = len(grades)
            average = summary/grades_size
            print(f"The average grades is {average}")
            return average

    def __init__(self,first_Name,last_Name):
      self.first_Name = first_Name
      self.last_Name = last_Name



