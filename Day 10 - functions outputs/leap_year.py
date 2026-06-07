def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Tests
assert is_leap_year(2000) == True
assert is_leap_year(2020) == True
assert is_leap_year(2024) == True
assert is_leap_year(2400) == True

assert is_leap_year(1700) == False
assert is_leap_year(1989) == False
assert is_leap_year(2100) == False

print("All tests passed!")