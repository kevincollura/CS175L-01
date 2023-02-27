'''
Kevin Collura
CS-175L
CalculateAverage
'''

def main():
    keep_going = True
    while(keep_going):
        score1, score2, score3, score4, score5 = enterScores()
        avg = calcAverage(score1, score2, score3, score4, score5)
        grade1,grade2,grade3,grade4,grade5,avgGrade = determineAll(score1, score2, score3, score4, score5, avg)
        printGrade(grade1,grade2,grade3,grade4,grade5,avg, avgGrade, score1, score2, score3, score4, score5)
        repeat = input("Enter 'yes' or 'y' to enter another input: ")
        if repeat == "yes" or repeat== 'y':
            keep_going = True
        else:
            keep_going = False
        
def enterScores():
    print("Enter 5 scores please.")
    score1 = int(input("Enter score 1:"))
    score2 = int(input("Enter score 2:"))
    score3 = int(input("Enter score 3:"))
    score4 = int(input("Enter score 4:"))
    score5 = int(input("Enter score 5:"))
    return score1, score2, score3, score4, score5

def calcAverage(score1, score2, score3, score4, score5):
    avg = (score1+score2+score3+score4+score5)/5
    return avg

def determine_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80 and score <90:
        grade = "B"
    elif score >= 70 and score <80:
        grade = "C"
    elif score >= 60 and score <70:
        grade = "D"
    else:
        grade = "F"
    return grade

def determineAll(score1, score2, score3, score4, score5, avg):
    grade1=determine_grade(score1)
    grade2=determine_grade(score2)
    grade3=determine_grade(score3)
    grade4=determine_grade(score4)
    grade5=determine_grade(score5)
    avgGrade = determine_grade(avg)
    return grade1,grade2,grade3,grade4,grade5,avgGrade

def printGrade(grade1,grade2,grade3,grade4,grade5, avg,avgGrade, score1, score2, score3, score4, score5):
    print()
    print(f'{"Score":<10}',f'{"Numeric Grade":<10}',f'{"Letter Grade":<10}')
    print("---------------------------------------------")
    print(f'{"Score 1:":<10}',f'{score1:<10}',f'{grade1:<10}')
    print(f'{"Score 2:":<10}',f'{score2:<10}',f'{grade2:<10}')
    print(f'{"Score 3:":<10}',f'{score3:<10}',f'{grade3:<10}')
    print(f'{"Score 4:":<10}',f'{score4:<10}',f'{grade4:<10}')
    print(f'{"Score 5:":<10}',f'{score5:<10}',f'{grade5:<10}')
    print(f'{"The Average Score is:":<10}',f'{avg:<10}',f'{avgGrade:<10}')

main()
