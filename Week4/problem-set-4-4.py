"""
Problem 4 - Hand Length
10.0/10.0 points (graded)
We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function.
This function allows the user to play out a single hand. First, though,
you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.
"""


def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    count = 0
    for key, value in hand.items():
        count += value
    return count
