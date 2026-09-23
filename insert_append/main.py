def add_to_front(items, value):
       slice = items[:]
       list_value = [value]
       new_list = list_value + slice
       return new_list

print(add_to_front([1, 2, 3], 6))        