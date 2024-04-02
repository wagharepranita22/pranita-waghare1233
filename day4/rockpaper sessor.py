# ROck paper scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_input=int(input("Enter your choice 0.rock 1.paper 2.scissors \n "))
if user_input==0:
    user=rock
    print(rock)
elif user_input==1:
    user = paper
    print(paper)
elif user_input==2:
    user = scissors
    print(scissors)
else:
    print("You have enter the invalid number")
    exit()

print("Computer choice")
random=random.randint(0,2)
print(f"Computer choice {random}")
if random==0:
    comp=rock
    print(rock)
elif random==1:
    comp=paper
    print(paper)
elif random==2:
    comp=scissors
    print(scissors)
else:
    print("You have enter the invalid number")
#
if user==rock and comp==rock:
    print("You have draw the match")
elif user==rock and comp==scissors:
    print("You win")
elif user==rock and comp==paper:
    print("You Lost")


if user==paper and comp==rock:
    print("You win")
elif user==paper and comp==scissors:
    print("You Lost")
elif user==paper and comp==paper:
    print("You have draw the match")


if user==scissors and comp==rock:
    print("You have lose")
elif user==scissors and comp==scissors:
    print("You have draw the match")
elif user==scissors and comp==paper:
    print("You win")
