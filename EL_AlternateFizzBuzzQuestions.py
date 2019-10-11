import math
#Alternate FizzBuzz Questions
#Number 1: Reverse a string
def reversestring(some_string):
    return ((some_string[:0:-1]).lower()+(some_string[0]).lower()).capitalize()
print(reversestring("Reverse me"))
#Number 2: Reverse a sentence ("bob likes dogs"->"dogs likes bob")
def reversesentence(some_string):
    sentence_as_list=some_string.split(" ")
    i=len(sentence_as_list)-1
    sentence_as_list_reversed=[]
    while i>=0:
        sentence_as_list_reversed.append(sentence_as_list[i])
        i-=1
    return " ".join(sentence_as_list_reversed)
print(reversesentence("bob likes dogs"))
#Number 3: Find the minimum value in a list
def findlistminimum(some_list):
    i=0
    j=1
    minimum=0
    while i<len(some_list)-1 and j<len(some_list):
        if some_list[i]<=some_list[j]:
            minimum=some_list[i]
            j+=1
        else:
            minimum=some_list[j]
            i=j
            j+=1
    return minimum
print(findlistminimum([0, 1, 2, 0, -1, 3, -5, 7, 2, 3, -8, -9, 10, 5]))
#Number 4: Find the maximum value in a list
def findlistmaximum(some_list):
    i=0
    j=1
    maximum=0
    while i<len(some_list)-1 and j<len(some_list):
        if some_list[i]>=some_list[j]:
            maximum=some_list[i]
            j+=1
        else:
            maximum=some_list[j]
            i=j
            j+=1
    return maximum
print(findlistmaximum([0, 1, 2, 0, -1, 3, -5, 7, 2, 3, -8, -9, 10, 5, 11]))
#Number 5: Calculate a remainder (given a numerator and  a denominator)
def calculateremainder(some_numerator, some_denominator):
    complete_parts=math.floor(some_numerator/some_denominator)
    return some_numerator-complete_parts*some_denominator
print(calculateremainder(5, 2))
#Number 6: Return distinct values from a list including duplicates
# (i.e. "1 3 5 3 7 3 1 1 5" -> "1 3 5 7")
def removeduplicates(some_list):
    new_some_list=[]
    for item in some_list:
        if item not in new_some_list:
            new_some_list.append(item)
    return new_some_list
print(removeduplicates([1, 3, 5, 3, 7, 3, 1, 1, 5]))
#Number 7: Return distinct values and their counts
# (i.e. the list above becomes "1(3) 3(3) 5(2) 7(1)")
def returncount(some_list):
    new_some_list=removeduplicates(some_list)
    item_counts=[]
    for item in new_some_list:
        item_counts.append(some_list.count(item))
    count_dictionary = {}
    for i in range(len(new_some_list)):
        count_dictionary[new_some_list[i]]=item_counts[i]
    return count_dictionary
print(returncount([1, 3, 5, 3, 7, 3, 1, 1, 5]))
#Number 8: Given a string of expressions (only variables, + and -)
#and a set of variable/value pairs (i.e. a=1, b=7, c=3, d=14)
#return the result of the expression ("a+b+c-d" would be -3)
def evaluateexpression(expression_string, variable_list):
    for item in variable_list:
        if item[0]=="a":
            a=int(item[2:])
        elif item[0]=="b":
            b=int(item[2:])
        elif item[0]=="c":
            c=int(item[2:])
        else:
            d=int(item[2:])
    return eval(expression_string)
print(evaluateexpression("a+b+c-d", ["a=1", "b=7", "c=3", "d=14"]))
    
    
            
