from hypot.calc import squared, addition, sqroot, hypot
import pytest


# test addition
## 4 + 7 = 11
def test_addition_int():
    assert addition(4, 7) == 11


## 2.3 + 7.92 = 10.22
def test_addition_float():
    assert addition(2.3, 7.92) == pytest.approx(10.22, 0.01)


## "a" + "b" = "Please use integer or float"
def test_addition_str():
    assert addition("a", "b") == "Please use integer or float"


# test squared


## 3^2 = 9 ## odd numbers
def test_squared_odd():
    assert squared(3) == 9


## 4^2 = 16 ## even numbers
def test_squared_even():
    assert squared(4) == 16


## (-2)^2 >0 ## negative numbers
def test_squared_negative():
    assert squared(-2) == 4


# test squared root
## sqroot(9) = 3
def test_sqroot():
    assert sqroot(9) == 3


# test hypotenuse
## 3,4 -> 5
def test_hypot():
    assert hypot(3, 4) == 5
