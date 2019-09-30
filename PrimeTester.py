#This program asks the user for an integer and tests whether this integer is a prime or not.
def primeornot():
    print ("Enter an integer:")
    user_input = input()
    user_input_int = int(user_input)
    is_prime = True
    for i in range(2, user_input_int-1):
        if user_input_int%i == 0:
            is_prime = False
    if is_prime:
        print ("{0} is a prime".format(user_input))
    else:
        print ("{0} is not a prime".format(user_input))
do_again = True
while do_again:
    print ("Ready to test whether an integer is a prime number or not (YES/NO)?")
    user_answer = input()
    if user_answer == "YES":
        primeornot()
        do_again = True
    elif user_answer == "NO":
        print ("Bye! Thanks for using PrimeTester!")
        do_again = False
    else:
        print ("Invalid input! Please try again!")
        do_again = True

