class MyHashSet:

    def __init__(self):
        self.set = [None] * 1000000
    
    def calc_hash_val(self, key):
        return key % 1000000
        
    def add(self, key: int) -> None:
        hash_val = self.calc_hash_val(key)
        if self.set[hash_val] is None:
            self.set[hash_val] = [key]
        else:
            self.set[hash_val].append(key)

    def remove(self, key: int) -> None:
        hash_val = self.calc_hash_val(key)
        if self.set[hash_val] != None:
            while key in self.set[hash_val]:
                self.set[hash_val].remove(key)
            

    def contains(self, key: int) -> bool:
        hash_val = self.calc_hash_val(key)
        if self.set[hash_val] != None: 
            return key in self.set[hash_val]
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)