from random import random

probability = 0.1


def validate(*args):
    random_num = random()
    if random_num < probability:
        raise Exception("Something went wrong!")
