from math import sin
from random import random
from hypothesis import given
from hypothesis.strategies import floats

def pathologic_sin(v):
    magic_value = random()
    return sin(v) + int(abs(v-magic_value) < 1e-2)

# defining smoothness as 
# "when the input value changes by epsilon, 
# the output value can't change more than epsilon",
# how would you test the smoothness of `sin` and `pathologic_sin`,
# and find where `pathologic_sin` is non-smooth?

# in this example, make sure to restrict your float range to between
# -1 and 1.

# hint: first implement the smoothness check at a specific value v :)

