class RandomizedSet:

    def __init__(self):
        self.vals = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.list.append(val)
        self.vals[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False

        idx = self.vals[val]
        last = self.list[len(self.list) - 1]
        self.list[idx] = last
        self.vals[last] = idx

        del self.list[len(self.list) - 1]
        del self.vals[val]
        return True



    def getRandom(self) -> int:
        idx = random.randint(0, len(self.list) - 1)
        return self.list[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()