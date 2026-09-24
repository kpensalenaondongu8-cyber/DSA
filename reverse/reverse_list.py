def reverse(items):

    new_list = []

    for item in range(len(items)-1, -1, -1):
        new_list.append(items[item])
    return new_list

all = [1, 2, 3, 4, 5, 6]
print(reverse(all))        
