def list_sum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

#print(listsum([1,3,5,7,9]))



#These test cases check that list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))
