n = input("Enter student name: ")

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

total = m1 + m2 + m3
avg = total / 3

print("Student Name:", n)
print("Total Marks:", total)
print("Average Marks:", avg)