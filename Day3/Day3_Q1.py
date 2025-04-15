#Q1
def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if type(item) is list:
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

list_input = [1, 2, 3, [1, 2, 3, [3, 4], 2]]
flat_list = flatten_list(list_input)
print(flat_list)



