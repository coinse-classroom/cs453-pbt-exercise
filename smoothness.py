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

def smooth_at_v(v, func):
    epsilon = random()*1e-2 - 5e-3
    return abs((func(v+epsilon)-func(v))/epsilon) < 1

@given(floats(min_value=-1, max_value=1))
def test_if_sin_smooth(v):
    assert smooth_at_v(v, sin)

@given(floats(min_value=-1, max_value=1))
def test_if_psin_smooth(v):
    assert smooth_at_v(v, pathologic_sin)