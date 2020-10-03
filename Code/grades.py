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

    count = len(grades)
    points = sum(grades.values())
    average = float(points / count)
  

    print(grades)
    print("Your average is: ", average)
    
main()
