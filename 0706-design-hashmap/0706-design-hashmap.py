class MyHashMap:

    def __init__(self):
        self.map = [None] * 100007
        
    def calc_hash_val(self, key):
        return key % 100007
        

    def put(self, key: int, value: int) -> None:
        hash_val = self.calc_hash_val(key)
        self.map[hash_val] = [key, value]
        # if self.set[hash_val] is None:
        #     self.set[hash_val] = [key, value]
        # else:
        #     self.set[hash_val].append(key)

    def get(self, key: int) -> int:
        hash_val = self.calc_hash_val(key)
        if self.map[hash_val] != None: 
            return self.map[hash_val][1] if key in self.map[hash_val] else -1
        return -1

    def remove(self, key: int) -> None:
        hash_val = self.calc_hash_val(key)
        self.map[hash_val] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)