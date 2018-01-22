input_list = [1,64]


def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.
    
    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    
    
    1.Check list length
    2. check if fewer than 3 elements, if so, return sorted largest to smallest
    3. if 3 or more elements, sort, then remove len - 3 from beginning

    # TODO: implement this function
    if len(input_list) < 3:
        print(input_list)
        return sorted(input_list(), reverse=True)
        print(input_list())
    else:
        top_threes = sorted(top_three)
        return top_threes[-3:]
        print(top_three())

print("XXX")
print(top_three(input_list))
print(input_list)
#print(top_three(input_list)
"""
    return sorted(input_list, reverse = True)[0:3]
