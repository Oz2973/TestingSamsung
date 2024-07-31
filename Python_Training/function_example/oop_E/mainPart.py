from Python_Training import driver
from Python_Training import lecture
from Python_Training import student


class mainPart():

    print("Test start")

    lecture_history = lecture("History")
    lecture_english = lecture("English")
    student_1 = student("Johan","Smith")
    student_2 = student("Haim","Cohen")
    driver_1 = driver("a")

    driver_1.print_speed(60)
    student_1.age_calculator(32)
    student_2.age_calculator(21)
    student_1.average_calc([67,37,90,100])

    student_1.age_printing_into_person(34)
    print("Test End")

