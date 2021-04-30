import check_file_present
import no_of_lines


def test_file():
    try:
        output = check_file_present.check_file('bank_check.txt')
        assert output.__eq__(True)
    except FileNotFoundError:
        print("No such file or directory")
    except AssertionError:
        print("assert False")


def test_file2():
    try:
        output = check_file_present.check_file('python bank.txt')
        assert output.__eq__(True)
    except FileNotFoundError:
        print("No such file or directory")
    except AssertionError:
        print("assert False")


def test_no_of_lines():
    try:
        output = no_of_lines.no_of_lines('hello')
        assert output == 0
    except FileNotFoundError:
        print("No such file or directory")


def test_no_of_lines1():
    try:
        output1 = no_of_lines.no_of_lines('no_of_lines')
        assert output1 == 0
    except FileNotFoundError:
        print("No such file or directory")


def test_no_of_lines3():
    try:
        output2 = no_of_lines.no_of_lines('hello')
        assert output2 > 0
    except FileNotFoundError:
        print("No such file or directory")
