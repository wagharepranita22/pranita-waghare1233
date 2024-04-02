number=int(input("Enter your numbers limit\n"))
total=0
for i in range(1,number+1):
    if i%2==0:
        total+=i
print(total)