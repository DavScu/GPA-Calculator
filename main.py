# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import curses

def GPA_Calculator():
    totalCredit = 0
    totalGrade = 0
    while True:
        credit = float(input("Enter credit: "))
        if credit == 10:
            print("Your GPA is: " + str(totalGrade/totalCredit))
            return
        grade = float(input("Enter grade: "))
        totalCredit += credit
        totalGrade += credit * grade



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    GPA_Calculator()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
