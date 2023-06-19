#WAP to print prime numbers in given range
lower=int(input("Enter lowest range"))
upper=int(input("Enter highest range"))
print("Prime numbers in the range are: ")
for number in range(lower,upper+1):
    if number>1:
        for i in range(2,number):
            if(number%i==0):
                break
            else:
                print(number)