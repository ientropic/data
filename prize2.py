
"""Defining points to be used as input for which_prize funtion"""
prize = None
points = 197

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
    elif points > 50 and points < 151:
        return "Oh dear, no prize this time."
    elif points < 181:
        prize = "wafer-thin mint"
    else:
        prize = "penguin"
    if prize:
        return "Congratulations! You have won a {}!".format(prize)
'''removed returns from each if/elif/ statement and added boolean to no prize
condition'''



"""
THIS is udacity's approach

def which_prize2(points):
    """
    Returns the number of prize-winning message, given a number of points
    """
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"

    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."

"""


    
print(which_prize(191))
