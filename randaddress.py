import json
import random


class AddressGenerator():
    def __init__(self):
        self.addresses = []
        self.max_length = 0

        with open("dataset/addresses-us-all.min.json", 'r') as f:
            data = json.load(f)
            addresses = data["addresses"]

            for address in addresses:
                if (
                    'address1' in address and
                    'city' in address and
                    'state' in address
                ):
                    addr_str = address['address1']
                    addr_str += ", "
                    addr_str += address['city']
                    addr_str += ", "
                    addr_str += address['state']
                    self.addresses.append(addr_str)

    def gen_address(self):
        index = random.randint(0, len(self.addresses) - 1)
        return self.addresses[index]

    def get_max_length(self):
        if self.max_length > 0:
            return self.max_length

        for addr in self.addresses:
            self.max_length = max(self.max_length, len(addr))

        return self.max_length