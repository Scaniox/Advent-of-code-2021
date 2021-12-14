from pathlib import Path
import re
from collections import Counter
import time

class linked_list():
    def __init__(self, start_list):
        self.uid = 10000
        self.data = {}
        self.start = self.uid
        self.length = len(start_list)

        previous_item = start_list[0]
        for item in list(start_list):
            self.data[self.uid] = [item, self.uid+1]
            self.uid += 1
            previous_item = item

        self.data[self.uid-1][1] = "END"

    def insert(self, index, new_item):
        if index > self.length:
            raise Exception("invalid index")

        self.length += 1

        if index == 0:
            self.data[self.uid] = [new_item, self.start]
            self.start = self.uid
        else:
            current_item = self.start
            for i in range(index-1):
                current_item = self.data[current_item][1]

            next_item = self.data[current_item][1]
            self.data[current_item][1] = self.uid
            self.data[self.uid] = [new_item, next_item]

        self.uid += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        return list_iterator(self.data.copy(), self.start, "END")

    def __repr__(self):
        return str(list(self))


class list_iterator():
    def __init__(self, list_data, start_point, end_point):
        self.data = list_data
        self.current_item = start_point
        self.end = end_point

    def __next__(self):
        if self.current_item == self.end:
            raise StopIteration
        value, self.current_item = self.data[self.current_item]
        return value


file_text = (Path(__file__).parent.parent / "14-input.txt").read_text()
template = re.match("([A-Z]+)\n", file_text).groups()[0]
rules = re.findall("([A-Z])([A-Z]) -> ([A-Z])", file_text)
rules = {(r[0], r[1]): r[2] for r in rules}

poly = linked_list(template)

for step in range(10):
    t1 = time.time()

    poly_iter = iter(poly)
    i = 0
    item_2 = next(poly_iter)
    while i < len(poly)-1:
        item_1 = item_2
        item_2 = next(poly_iter)
        i += 1

        if (item_1, item_2) in rules:
            new_monomer = rules[(item_1, item_2)]
            poly.insert(i, new_monomer)
            i += 1

    print(f"step {step} took: {time.time() - t1}")

counts = Counter(poly)
ans = max(counts.values()) - min(counts.values())
print(ans)
