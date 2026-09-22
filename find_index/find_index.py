def find_index(item, target):
    for x, items in enumerate(item):
        if target not in items:
            return -1
        else:
            return target[x]


all = find_index(["hello","how", "are", "you", "doing"], "you")
print(all)