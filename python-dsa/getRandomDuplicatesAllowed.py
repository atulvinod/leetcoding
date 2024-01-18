import random

class RandomizedCollection:

    def __init__(self):
        self.collectionSet = set()
        self.collectionMap = dict()

    def insert(self, val: int) -> bool:
        if val in self.collectionMap:
            self.collectionMap[val] += 1
            return False
        self.collectionSet.add(val)
        self.collectionMap[val] = 1

    def remove(self, val: int) -> bool:
        if val not in self.collectionMap:
            return False
        if self.collectionMap[val] == 1:
            del self.collectionMap[val]
            self.collectionSet.remove(val)
            return True
        else:
            self.collectionMap[val] -= 1

    def getRandom(self) -> int:
        random_element = random.sample(self.collectionSet, 1)[0]
        return random_element


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()