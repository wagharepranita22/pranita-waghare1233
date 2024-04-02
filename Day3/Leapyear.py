# Leap year
print("Welcome to leap year calculator")
year=int(input("Please enter your year \n"))
print(f"your gonna  verify the {year} ")
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Year is leap year")

else:
    print("year is not leap year")