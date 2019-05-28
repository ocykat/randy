import random


def gen_phonenumber(length=10, prefix=""):
    res = prefix
    cur_length = len(prefix)

    while cur_length < length:
        res += str(random.randint(0, 9))
        cur_length += 1

    return res
