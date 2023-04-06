

current_year = 2023 #global variable

def is_student_adult(): #this function calculates the age of student and returns true or false
    name = input("input your name: ")
    date_of_birth = int(input("input year of birth: "))
    age = current_year  -  date_of_birth
    if age >= 18:
        print(bool(age))
    else:
        print(False)



is_student_adult()
