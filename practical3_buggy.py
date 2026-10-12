def calculate_grade(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    return average, grade


marks = []

for i in range(3):
    mark = float(input("Enter marks: "))

    if mark < 0 and mark > 100:
        print("Invalid marks")
    marks.append(mark)

average, grade = calculate_grade(mark)

print("Average:", average)
print("Grade:", grade)