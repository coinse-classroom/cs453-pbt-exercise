from hypothesis import given
from hypothesis.strategies import text

# example taken from Hypothesis quickstart
# (https://hypothesis.readthedocs.io/en/latest/quickstart.html)
# is given. 

# below, a lossless encoding-decoding algorithm is provided.

def encode(input_string):
    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

# We want to know that the decode function is indeed the
# inverse of the encode function. How would we express this in
# hypothesis?
