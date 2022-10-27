from LeapYear import isLeapYear

# The year in this test is divisble by 400.
def test_isLeapYear_divisible_by_400() -> None:
    assert isLeapYear(2000)

# The year in this test is divisible by 4, but not 100.
def test_isLeapYear_divisible_by_4_not_100() -> None:
    assert isLeapYear(2040)

# The year in this test is not divisible by 4.
def test_isLeapYear_not_divisible_by_4() -> None: 
    assert not isLeapYear(2005) # assert not, because this is supposed to return False

# This test is checking if a year that is divisble by 100, but not 400 is a leap year.
def test_isLeapYear_divisble_by_100_not_400() -> None:
    assert not isLeapYear(1800) # assert not, because this is supposed to return False