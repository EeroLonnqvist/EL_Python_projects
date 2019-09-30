#In this program the user gets the chance to test whether a list of integers contains Pythagorean triples or not
#If yes then the program counts the total number of triples there are
empty_list=[]
def create_list():
    more=True
    counter_1=0
    while more:
        print ("Enter an integer:")
        user_int=int(input())
        empty_list.append(user_int)
        counter_1=counter_1+1
        print ("Do you want to enter another integer (Y/N)?")
        user_response=input()
        if user_response == "Y":
            more=True
        elif user_response == "N" and counter_1>=3:
            more=False
        else:
            more=True
            print ("You need to enter at least three integers in total!")
    else:
        return empty_list
    
def check_list(random_list):
    counter_2=0
    new_empty_list=[]
    for i in random_list:
        for j in random_list:
            for k in random_list:
                if i**2+j**2==k**2 and [j, i, k] not in new_empty_list:
                    new_empty_list.append([i, j, k])
                    counter_2=counter_2+1 
    print ("Here is a list with all Pythagorean triples that your list contains:")
    print (new_empty_list)
    print ("In total your list contains {0} Pythagorean triples".format(counter_2))
    
print ("Are you ready to use PythagoreanTriples (Y/N)?")
user_answer=input()
while user_answer=="Y":
    create_list()
    check_list(empty_list)
    print ("Do you want to check another list of integers (Y/N)?")
    user_reaction=input()
    if user_reaction=="Y":
        user_answer=="Y"
        empty_list=[]
    else:
        print("Thank you for using PythagoreanTriples and bye!")
        break
