#This program prompts the user for an integer and performs the classic FizzBuzz behaviour until that integer. 
print ("Do you want to proceed? Enter Y for yes or N for no:")
user_decision = input()
while user_decision=="Y":
    print ("Enter an integer:")
    user_int = input()
    print ("You just entered: "+user_int)
    for i in range(1, int(user_int)+1):
        if i%15==0:
            print ("FizzBuzz")
        elif i%5==0:
            print ("Buzz")
        elif i%3==0:
            print ("Fizz")
        else:
            print (i)
    print ("Do you want to proceed? Enter Y for yes or N for no:")
    user_decision = input()
print ("Thank you for using FizzBuzz and bye!")
    
