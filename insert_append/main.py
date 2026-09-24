def add_to_front(items, value):
    #    slice = items[:]
    #    list_value = [value]
    #    new_list = list_value + 
       items = [value] + items
       return items

original = [1, 2, 3]
print(original)
print(add_to_front(original, 6))  
