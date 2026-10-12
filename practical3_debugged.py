def calculate_grade(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    return average, grade


marks = []

while len(marks) < 3:
    subject_number = len(marks) + 1

    try:
        mark = float(input(f"Enter marks for subject {subject_number}: "))
    except ValueError:
        print("Please enter a numeric mark.")
        continue

    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a mark from 0 to 100.")
        continue

    marks.append(mark)

average, grade = calculate_grade(marks)

print("Average:", average)
print("Grade:", grade)