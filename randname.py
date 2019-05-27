import random


class NameGenerator:
    def __init__(self):
        self.male_fnames   = []
        self.female_fnames = []
        self.fnames = []
        self.lnames = []

        with open("dataset/first-names.txt", 'r') as f:
            for line in f:
                fname = line[:-1]
                self.fnames.append(fname)

        with open("dataset/names.txt", 'r') as f:
            for line in f:
                lname = line[:-1]
                self.lnames.append(lname)

        with open("dataset/female-names.txt", 'r') as f:
            for line in f:
                fname = line[:-1].capitalize()
                self.female_fnames.append(fname)

        with open("dataset/male-names.txt", 'r') as f:
            for line in f:
                fname = line[:-1].capitalize()
                self.male_fnames.append(fname)

    def gen_fname(self, gender=None):
        if gender == 'male':
            index = random.randint(0, len(self.male_fnames) - 1)
            return self.male_fnames[index]
        elif gender == 'female':
            index = random.randint(0, len(self.female_fnames) - 1)
            return self.female_fnames[index]
        else:
            index = random.randint(0, len(self.fnames) - 1)
            return self.fnames[index]

    def gen_lname(self):
        index = random.randint(0, len(self.lnames) - 1)
        return self.lnames[index]