def main():
    homework_score = [39,40,29,40,0,5]
    homework_max = [40,40,40,40,40,5]
    quizzes_score = [10,10,9,2,10,10,10]
    quizzes_max = [10,10,10,10,10,10,10]
    test_score = [293,284,300]
    test_max = [300,300,300]
    homework = 0.20
    quizzes = 0.20
    test = 0.60
    hw_avg = round(average(homework_score, homework_max))
    quiz_avg = round(average(quizzes_score, quizzes_max))
    test_avg = round(average(test_score, test_max))
    hwk_letter = letter_grade(hw_avg)
    quiz_letter = letter_grade(quiz_avg)
    test_letter = letter_grade(test_avg)
    hw_weight = average_weighted(homework_score, homework_max, homework)
    quiz_weight = average_weighted(quizzes_score, quizzes_max, quizzes)
    test_weight = average_weighted(test_score, test_max, test)
    final_perc = (hw_weight + quiz_weight + test_weight)
    final_letter = letter_grade(final_perc)
    print("Homework Grade: " , hw_avg , hwk_letter)
    print("Quiz Grade: " , quiz_avg , quiz_letter)
    print("Test Grade: " , test_avg , test_letter)
    print("Final Grade: " , round(final_perc) , final_letter)
def average (score_list,max_list):
    score = ((sum(score_list)/sum(max_list))*100)
    return (score)
    
def letter_grade(percent):
    if (percent >= 90 and percent <= 100):
        return "A"
    elif (percent >= 80 and percent <= 89):
        return "B"
    elif (percent >= 70 and percent <= 79):
        return "C"
    elif (percent >= 60 and percent <= 69):
        return "D"
    elif (percent >= 50 and percent <= 59):
        return "F"

def average_weighted(score_list, max_list, weight):
    return (average(score_list, max_list))*weight
main()
    

