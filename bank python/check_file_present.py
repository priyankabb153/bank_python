from os import path
import pytest


def check_file(name):
    return path.exists(name)
