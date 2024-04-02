student_marks=input().split()

for i in range(0,len(student_marks)):
    student_marks[i]=int(student_marks[i])

highest_marks=0
for marks in student_marks:
    if marks>highest_marks:
        highest_marks=marks


print(f"The highest marks of the class are {highest_marks}")