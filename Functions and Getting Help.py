# Functions and Getting Help
#
# 1.
def round_to_two_places(num):
    return round(num, 2)

# 3.
def to_smash(total_candies, n_friends = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n_friends

# 4.
print(round_to_two_places(9.9999))
x = -10
y = 5
smallest_abs = min(abs(x), abs(y))
print(smallest_abs)
def f(x):
    y = abs(x)
    return y
print(f(5))