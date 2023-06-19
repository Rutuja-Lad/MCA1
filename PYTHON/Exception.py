class Error():
    while True:
        try:
            age=int(input("Enter your age for election: "))
            if age<18:
                raise AgesmallException
            else:
                print("you are eligible for voting")
        
                break
        except AgesmallException:
            print("This value is too small,try again!")
            print()    