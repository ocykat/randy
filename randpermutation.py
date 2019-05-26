import random


def shuffle(a):
    """Shuffle an array using Fisher-Yates algorithm
    Args:
        a: array
    """
    for i in range(len(a) - 1):
        j = random.randint(i, len(a) - 1)
        a[i], a[j] = a[j], a[i]


def gen_combination(a, k):
    """Generate a random combination of size k from an array a
    Args:
        a: array
        k: size of the output combination
    """
    shuffle(a)
    res = []

    assert k <= len(a)

    for i in range(k):
        j = random.randint(i, len(a) - 1)
        a[i], a[j] = a[j], a[i]
        res.append(a[i])

    return res