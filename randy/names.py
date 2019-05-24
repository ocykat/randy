import random


class NameGenerator:
    def __init__(self):
        self.fnames = []
        self.lnames = []

        with open("dataset/first-names.txt", "r") as f:
            for line in f:
                fname = line[:-1]
                self.fnames.append(fname)

        with open("dataset/names.txt", "r") as f:
            for line in f:
                lname = line[:-1]
                self.lnames.append(lname)

    def gen_fname():
        index = random.randint(0, len(self.fnames) - 1)
        return self.fnames[index]

    def gen_lname():
        index = random.randint(0, len(self.lnames) - 1)
        return self.lnames[index]
