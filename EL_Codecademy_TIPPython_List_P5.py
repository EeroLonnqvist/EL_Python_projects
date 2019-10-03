# remove duplicates 
# no time/space requirements
# return a list with duplicates removed

def remove_duplicates(dupe_list):
    empty_list=[]
    for i in dupe_list:
        if i not in empty_list:
            empty_list.append(i)
    return empty_list



#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']), ['a', 'x', 'g', 't'], remove_duplicates(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']) == ['a', 'x', 'g', 't']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']), ['c', 'd', 'e', 'f', 'a'], remove_duplicates(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'a', 'a']) == ['c', 'd', 'e', 'f', 'a']))

print("{0}\n should equal \n{1}\n {2}\n".format(remove_duplicates([13, 13, 13, 13, 13, 42]), [13, 42], remove_duplicates([13, 13, 13, 13, 13, 42]) == [13, 42]))
