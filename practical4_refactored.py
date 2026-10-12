def report_average_result(first_score, second_score, third_score):
    average_score = (first_score + second_score + third_score) / 3

    if average_score >= 50:
        print("Pass")
    else:
        print("Fail")

    print(average_score)


report_average_result(70, 60, 80)