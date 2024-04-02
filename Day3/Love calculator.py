name1=input("Please enter your name \n")
name2=input("Please enter their  name\n")
comb=name1+name2
comb=comb.lower()
t=comb.count('t')
r=comb.count('r')
u=comb.count('u')
e=comb.count('e')
t1=t+r+u+e
l=comb.count('l')
o=comb.count('o')
v=comb.count('v')
e=comb.count('e')
t2=l+o+v+e

t1=str(t1)
t2=str(t2)
t_count=t1+t2
t_count=int(t_count)
if t_count <= 10 or t_count > 90:
    print(f"your love score if {t_count},you go together like coke and mentos")
elif t_count in range (40,50):
    print(f"Your love score {t_count}, your alright together")
else:
    print(f"your love score is {t_count}")