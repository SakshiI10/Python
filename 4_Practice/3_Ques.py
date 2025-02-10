my_dict = {'a': 4, 'b': 5, 'd': 7}
def manipulate_dict(input_dict):
    input_dict['c'] = 6  # Add key 'c' with value 6
    for key in input_dict:
        input_dict[key] += 2  # Increment all values by 2
    input_dict['d'] = 0  # Set 'd' to 0
    return input_dict

result = manipulate_dict(my_dict)
print(result)
