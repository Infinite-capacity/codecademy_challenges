#!/usr/bin/env


def large_power(base, exp):
    if base ** exp > 5000:
        return True
    else:
        return False


def over_budget(budget, food, electricity, internet, rent):
    if budget >= food + electricity + internet + rent:
        return "You are within budget!"
    else:
        return "You are over budget!"


def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


def not_sum_to_ten(num1, num2):
    if not num1 + num2 == 10:
        return True
    else:
        return False


print("Large power result: " + str(large_power(500, 20)))
print("Over budget result: " + str(over_budget(2000, 200, 150, 50, 925)))
print("Twice as large result: " + str(twice_as_large(100, 49)))
print("Divisible by ten result: " + str(divisible_by_ten(11)))
print("Not sum to ten result: " + str(not_sum_to_ten(5, 5)))
