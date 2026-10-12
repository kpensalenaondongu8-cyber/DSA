counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)   