#This program prompts the user for a natural number n and enters the n-th Fibonacci number
def choice_checker(possible_integer):
    if type(possible_integer)!=int or possible_integer<=0:
        print ("Invalid input! Please try again. ")
        return False
    else:
        return True
def right_fibonacci(integer):
    if integer==0:
        return 0
    elif integer==1 or integer==2:
        return 1
    else:
        return right_fibonacci(integer-2)+right_fibonacci(integer-1)
def fibonacci_search():
    print ("Enter a natural number (Positive integer and greater than 0): ")
    user_choice = int(input())
    if choice_checker(user_choice):
        print ("You chose the number {}. The corresponding Fibonacci number is {}. ".format(user_choice, right_fibonacci(user_choice)))
    else:
        print ("Remember to enter a natural number (Positive integer and greater than 0)! ")
whether_again=True
while whether_again:
    fibonacci_search()
    print ("Do you want to try this for another number (Y/N)?")
    user_answer=input()
    if user_answer=="N":
        whether_again=False
        print ("Thank you for using FibonacciSearch and bye! ")
        


        
