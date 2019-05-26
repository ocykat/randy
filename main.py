import json
from randname import NameGenerator
from randpermutation import gen_combination
from randdatetime import gen_date
from randaddress import AddressGenerator


# name_gen = NameGenerator()

# a = [i for i in range(10)]

# print(gen_combination(a, 5))

# print(gen_date(year_range_lower=1970, year_range_upper=1980))


addr_gen = AddressGenerator()
print(addr_gen.gen_address())
print(addr_gen.get_max_length())