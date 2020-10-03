# enter grades for subjects and then return the average
# ask the user to select a subject and change the grade

def main():
    
    english_grade = int(input("Enter English Grade: "))
    maths_grade = int(input("Enter Maths Grade: "))
    globalstudies_grade = int(input("Enter Global Studies Grade: "))
    art_grade = int(input("Enter Art Grade: "))
    music_grade = int(input("Enter Music Grade: "))


    grades = {
        "English": english_grade,
        "Maths": maths_grade,
        "Global Studies" : globalstudies_grade,
        "Art" : art_grade,
        "Music": music_grade
            }

    average = float(sum(grades.values()) / len(grades))
  

    print(grades)
    print("Your average is: ", average)

    new_grade_subject = input("Which grade would you like to change? ")
    new_grade = int(input("What is the new grade? "))

    grades[new_grade_subject] = new_grade
    average = float(sum(grades.values()) / len(grades))

    print("Your new average is: ", average)
    
main()
