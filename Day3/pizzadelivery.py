print("Welcome to the pizza delivery system")
size=input("please enter what size of pizza do you want  s,m or l\n")
add_pepperoni=input("Do you want to add pepperoni y or n\n")
extra_cheese =input("DO you want to extra cheese  y or n\n")
bill=0
if size=='l':
    bill=25
elif size=='m':
    bill=20
elif size=="s":
    bill=15
else:
    print("you have enter the wrong input")


if add_pepperoni=='y':
    bill+=2

if extra_cheese=='y':
    bill+=1

print(f"Your total bill will be {bill}")