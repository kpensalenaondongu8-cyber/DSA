def find_index(items, target):
    for ind, val in enumerate(items):
        if val == target:
            return f"{val} is at index {ind}"
        
    return -1


all = find_index(["hello", "how", "you", "doing", "dear"], "you")
print(all)