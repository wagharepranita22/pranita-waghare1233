import random
name=input("enter name seprated by , \n")
name=name.split(",")
name=list(name)
print(name)
pick=random.randint(0,len(name))
print(f"{name[pick]} is gonna pay for meal")
