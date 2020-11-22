#!/usr/bin/env


def in_range(num, lower, upper):
    if lower <= num <= upper:
        return True
    else:
        return False


def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False


def always_false(num):
    if num >= 1 or num <= 1:
        return False


def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif 5 < rating < 9:
        return "This one was fun."
    elif rating >=9:
        return "Outstanding!"


def max_num(num1, num2, num3):
    if num1 <= num3 and num2 <= num3:
        if num1 == num3 > num2:
            return "It's a tie!"
        if num2 == num3 > num1:
            return "It's a tie!"
        else:
            return num3
    elif num1 <= num2 and num3 <= num2:
        if num1 == num2 > num3:
            return "It's a tie!"
        if num2 == num3 > num1:
            return "It's a tie!"
        else:
            return num2
    elif num3 <= num1 and num2 <= num1:
        if num1 == num3 > num2:
            return "It's a tie!"
        if num2 == num1 > num3:
            return "It's a tie!"
        else:
            return num1
