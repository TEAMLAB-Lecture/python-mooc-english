# -*- coding: utf-8 -*-


# Get the number of subjects from a console
def get_number_of_subjects():

    # """
    # Input:
    # 	- None
    # Output:
    # 	- number_of_subjects:  number of subjects, Integer Type
    # Examples(python shell):
    # 	>>> import exam_grader as eg
    # 	>>> eg.get_number_of_subjects()
    #   Enter the number of subjects: 10
    #   10
    # """
    #
    # ===Modify codes below=================
    number_of_subjects = None
    # ======================================
    return number_of_subjects


# Help Funtion - Do not modify this one
def sum_of_scores(number_of_subjects):

    total_score = 0
    for i in range(number_of_subjects):
        message = "Enter the score of the " + str(i + 1) +" subject: "
        score = int(input(message))
        total_score = total_score + score
    return total_score


# Help Funtion - Do not modify this one
def print_exam_grader(average_score):
    grade = 'F'
    if average_score >= 90.0:
        grade = 'A'
    elif average_score >= 80.0:
        grade = 'B'
    elif average_score >= 70.0:
        grade = 'C'
    elif average_score >= 60.0:
        grade = 'D'
    else:
        grade = 'F'
    print("Average: ", average_score)
    print("Grade: ", grade)

def main():
    print("Start of Exam Grader Program")
    print("============================")

    number_of_subjects = get_number_of_subjects()
    total_score = sum_of_scores(number_of_subjects)
    average_score = get_average_score(
        total_score=total_score, number_of_subjects=number_of_subjects)
    print_exam_grader(average_score)

    print("===========================")
    print("End of Exame Grader Program")

if __name__ == '__main__':
    main()
