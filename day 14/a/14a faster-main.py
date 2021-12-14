from pathlib import Path
import re
from collections import Counter
import time

class polymer():
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

    def polymerise(self, rules):
        misses = 0

        item2_id = self.start
        item2_n = self.data[self.start][0]
        while True:
            item1_id = item2_id
            item2_id = self.data[item2_id][1]
            if item2_id == "END":
                break

            item1_n = item2_n
            item2_n = self.data[item2_id][0]

            if (item1_n, item2_n) in rules:
                new_item_n = rules[(item1_n, item2_n)]
                new_item_id = self.uid
                self.uid += 1

                self.data[new_item_id] = [new_item_n, item2_id]
                self.data[item1_id] = [item1_n, new_item_id]
                item1_n, item1_id = new_item_n, new_item_id
            else:
                misses += 1


        return misses


    def __len__(self):
        return self.length

    def __iter__(self):
        return list_iterator(self.data.copy(), self.start, "END")

    def __repr__(self):
        return "".join(list(self))


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

poly = polymer(template)

for step in range(10):
    t1 = time.time()
    misses = poly.polymerise(rules)
    if step < 5:
        print(poly)

    print(f"step {step} took: {time.time() - t1}")

counts = Counter(poly)
ans = max(counts.values()) - min(counts.values())
print(ans)
