class HashTable:

    def __init__(self, size=8):
        self.size = size
        self.buckets = [[]for _ in range(size)]
        self.count = 0

    def index(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        bucket = self.buckets[self.index(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        bucket = self.buckets[self.index(key)]
        for k, v in bucket:
            if k == key:
                return v

        return None

    def delete(self, key):
        bucket = self.buckets[self.index(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
        return None                            

    def __contains___(self, key):
        bucket = self.buckets[self.index(key)]
        for k, v in bucket:
            if k == key:
                return True
        return False

    def __len__(self):
        return self.count

words = "the cat and the dog and the bird".split()

counts = HashTable()

for word in words:
   current = counts.get(word)

   if current is None:
       current = 1
   else:
       current += 1

   counts.set(word, current)           


print(counts.get("the"))
print(counts.get("and"))
print(counts.get("bird"))