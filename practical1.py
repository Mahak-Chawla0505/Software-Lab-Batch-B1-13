"""Calculate a student's total and average marks across three subjects."""

name = input("Enter the student's name: ")
marks = [float(input(f"Enter marks for subject {subject}: ")) for subject in range(1, 4)]

total = sum(marks)
average = total / 3

# Calculates the total and average marks, and displays the student's result.
print(f"Student: {name}")
print(f"Total marks: {total:g}")
print(f"Average marks: {average:.2f}")

