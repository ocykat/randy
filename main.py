from randy.names import NameGenerator
from randy.permutations import gen_combination
from randy.datetime import gen_date


name_gen = NameGenerator()

a = [i for i in range(10)]

print(gen_combination(a, 5))

print(gen_date(year_range_lower=1970, year_range_upper=1980))