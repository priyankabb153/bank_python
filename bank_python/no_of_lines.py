import pytest1


def no_of_lines(filename):
    file = open(filename, "r")
    counter = 0
    lines = file.read()
    count = lines.split("\n")
    # print(count)
    for i in count:
        if i:
            counter += 1

    return counter
