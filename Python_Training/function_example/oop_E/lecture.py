from Python_Training import person


class lecture(person):

    def __init__(self,type):
        self.type = type

    def tax_calculator(self,salary,tax):
        salary_last = salary*(100-tax)/100
        return salary_last
