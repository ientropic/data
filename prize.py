
"""Defining points to be used as input for which_prize funtion"""
points = 123

"""
Points	Prize
0 - 50	wooden rabbit
51 - 150	No prize
151 - 180	wafer-thin mint
181 - 200	penguin


"""
def which_prize(points):
    if points < 51:
        prize = "wooden rabbit"
        return "Congratulations! You have won a {}!".format(prize)
    elif points < 151:
        prize = "none"
        return "Oh dear, no prize this time."
    elif points < 181:
        prize = "wafer-thin mint"
        return "Congratulations! You have won a {}!".format(prize)
    else:
        prize = "penguin"
        return "Congratulations! You have won a {}!".format(prize)

    
print(which_prize(121))
