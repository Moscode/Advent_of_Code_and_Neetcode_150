class RandomizedSet:

    def __init__(self):
        self.store = set()

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        self.store.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.store:
            self.store.remove(val)
            return True
        return False