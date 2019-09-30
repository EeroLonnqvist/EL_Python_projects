#This program asks the user for an integer and searches the next prime number
#This time the program uses the so called square root method for testing
import math
print ("Enter an integer:")
user_prompt=int(input())
possible_prime=user_prompt+1
tester=True
def prime_check(truthy, integer):
    for i in range(2, math.ceil(math.sqrt(integer))):
        if integer%i==0:
            truthy=False
    return truthy
while not prime_check(tester, possible_prime):
    possible_prime=possible_prime+1
else:
    print ("The next prime number is: {0}".format(possible_prime))
