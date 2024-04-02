height=int(input("Please enter your height \n "))
bill=0
if height>120:
    print("you can ride")
    age=int(input("please entr your age\n"))
    if age >18:
        print("Please pay the 18 $")
        bill=18
    elif 12< age <= 18 :
        print("Please pay 7$")
        bill=7
    elif age <= 12:
        print("please pay the 5$")
        bill=5
    w_photo=input("If you want the photo of your ride then enter 'y' and if dont want then enter 'n' ")
    if w_photo=='y':
        bill+=3
    print(f"Your total bill is {bill}")

else :
    print("Sorry ! you can not ride")

