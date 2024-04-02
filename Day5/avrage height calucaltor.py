# Average hight
from typing import List

student_heigths=input().split()

for i in range(0,len(student_heigths)):
    student_heigths[i]=int(student_heigths[i])

total_height=0
for height in student_heigths:
    total_height+=height
print(f"Total height={total_height}")

total_of_student=0
for student in student_heigths:
    total_of_student+=1
print(f"Total number of student ={total_of_student}")


average_of_students=round(total_height/total_of_student)
print(f"Avreage of student ={average_of_students}")