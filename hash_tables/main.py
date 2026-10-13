class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.bucket = [[]for _ in range(size)]
        self.count = 0

    def index(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        bucket = self.bucket[self.index(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        bucket = self.bucket[self.index(key)]
        for k, v in bucket:
            if k == key:
                return v
        return None                    
        
    def delete(self, key):
        bucket = self.bucket[self.index(key)]
        for i, (k, v) in enumerate(bucket):
         if k == key:
           del bucket[i]
           self.count -= 1

        return None

    def __contains__(self, key):
       bucket = self.bucket[self.index(key)]
       for k, v in bucket:
            if k == key:
                return True
       return False  

    def __len__(self):
       return self.count



ht = HashTable()
ht.set("cat", 3)
ht.set("ace", 7)
ht.set("cat", 8)
print(ht.get("cat"))    
print(ht.get("ace"))    
ht.delete("ace")
print(ht.get("ace")) 
print("cat" in ht)
print(len(ht))  
print("dog" in ht) 