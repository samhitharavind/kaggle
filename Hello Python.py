# Hello Python
# 
# Intro
print("You've successfully run some Python code")
print("Congratulations!")

# 0.
color = "blue"

# 1.
pi = 3.14159
diameter = 3
radius = 0.5 * diameter
area = pi * (radius ** 2)
print(area)

# 2.
a = [1, 2, 3]
b = [3, 2, 1]
tmp = a
a = b
b = tmp
print(a)
print(b)

# 3.
c = (5 - 3) // 2
print(c)
d = (8 - 3) * (2 - (1 + 1))
print(d)

# 4.
alice_candies = 121
bob_candies = 77
carol_candies = 109
to_smash = (alice_candies + bob_candies + carol_candies) % 3
print(to_smash)
