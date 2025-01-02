from ftplib import print_line
from functools import total_ordering


def calculate_love_score(name1,name2):
    first = "True"
    second = "LOVE"
    total = 0
    total2 = 0
    for letter in first.lower():
        for letter2 in name1.lower():
            if letter == letter2:
                total = total + 1
    for letter in first.lower():
        for letter2 in name2.lower():
            if letter == letter2:
                total = total + 1

    print(total,end="")

    for letter3 in second.lower():
        for letter4 in name1.lower():
            if letter3 == letter4:
                total2 = total2 + 1
    for letter3 in second.lower():
        for letter4 in name2.lower():
            if letter3 == letter4:
                total2 = total2 + 1
    print(total2)



calculate_love_score("Angela Yu", "Jack Bauer")

