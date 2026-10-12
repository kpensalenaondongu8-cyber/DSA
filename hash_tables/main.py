def toy_hash(key):
    total = 0
    for ch in key:
        total += ord(ch)      
    return total % 5         

print(toy_hash("dat"))
print(toy_hash("cat"))   
print(toy_hash("dog"))   
print(toy_hash("pig"))
print(toy_hash("hen"))