def remove_duplicate(numbers):
    new_list = []

    for item in numbers:
        if item not in new_list:
            new_list.append(item)  
    return new_list


all = [1, 2, 2, 3, 1, 4]
num = ["hello", "ada", "how", "you", "doing", "you"]
print(remove_duplicate(num))
print(remove_duplicate(all))
