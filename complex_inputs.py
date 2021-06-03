from hypothesis import given
from hypothesis.strategies import builds, integers, lists
from itertools import zip_longest

# we can use hypothesis to sample from types other than
# the ones provided by the library. Consider:

class MyComplex():
    def __init__(self, a: int, b: int):
        self._a = a
        self._b = b
    
    def coord_sum(self):
        return self._a + self._b
    
    def size(self):
        return (self._a**2 + self._b**2)**0.5
    
def complex_add(n1: MyComplex, n2: MyComplex):
    return MyComplex(
        n1._a + n2._a,
        n1._b + n2._b
    )

# we can sample random MyComplex arguments and test `complex_add`
# with the following:

@given(builds(MyComplex, integers()), builds(MyComplex, integers()))
def test_complex_add(n1, n2):
    n_add = complex_add(n1, n2)
    assert n_add.coord_sum() == (n1.coord_sum() + n2.coord_sum())

# Now, consider the following implementation of a polynomial
# and its addition function:

class Polynomial():
    def __init__(self, coefficients: list):
        assert 1 <= len(coefficients) <= 6
        self._coeffs = coefficients
    
    def degree(self):
        if all(map(lambda x: x == 0, self._coeffs)):
            return 0
        else:
            return max(i for i, c in enumerate(self._coeffs) if c != 0)
    
    def __repr__(self):
        if all(map(lambda x: x == 0, self._coeffs)):
            return '0x^0'
        else:
            mono_strs = [f'{c}x^{i}' for i, c in enumerate(self._coeffs) if c != 0]
            return '+'.join(mono_strs)


def polynomial_add(p1: Polynomial, p2: Polynomial):
    new_coeffs = [a+b for a, b in zip_longest(p1._coeffs, p2._coeffs, fillvalue=0)]
    return Polynomial(new_coeffs)

# write the test function that generates polynomials and tests the
# property that when adding two polynomials, the degree of the new
# polynomial cannot exceed that of the two added polynomials.

@given(builds(Polynomial, lists(integers(), min_size=1, max_size=6)),
       builds(Polynomial, lists(integers(), min_size=1, max_size=6)))
def test_polynomial_add(p1, p2):
    new_polynomial = polynomial_add(p1, p2)
    assert new_polynomial.degree() <= max(p1.degree(), p2.degree())

# you can also use this formulation to see a weakness of hypothesis:
# while the degree of the new polynomial does not have to be *exactly*
# the maximum degree of the two added polynomials (consider -x and x), 
# hypothesis fails to find a counterexample for that property.