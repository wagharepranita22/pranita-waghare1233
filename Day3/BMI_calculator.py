print("Welcome to the bMI weight calculator")
weight=float(input("Please enter your weight\n"))
height=float(input("Please enter your height\n"))
bmi=(weight/(height*height))

print(f"your Bmi {bmi}")
if bmi<18.5:
    print(f"your BMI is {bmi},your slightly underweight")
elif 18.5<bmi<25:
    print(f"your bmi is {bmi},you have normal weight")
elif 25< bmi <30:
    print(f"your bmi id {bmi},your slightly overweight")
elif 30 <bmi<35:
    print(f"your bmi is {bmi},your obese")
elif bmi>35:
    print(f"you bmi is {bmi},you are clinically obese")