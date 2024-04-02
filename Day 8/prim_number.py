# primnumber
def prime_number(number):
    count=0
    for i in range(1,number+1):
        if number%i==0:
            print(i)
            count+=1
    print(count)
    if count==2:
        print("number is prime")
    else:
        print("Number is not prime")


number=int(input("Number : "))
prime_number(number)