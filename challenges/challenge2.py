'''
write a function, which takes three integers a, b, and c as arguments, 
and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.
'''
def exactly_two_positive(a, b, c):
    # Count the number of positive integers
    positive_int_count = 0

    if a > 0: 
        positive_int_count = +1
    if b > 0:
        positive_int_count = +1
    if c > 0:
        positive_int_count = +1

        #Check if exactly two of the integers are positive
    return positive_int_count == 2             