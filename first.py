# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].

def pick_from_list(list_in):
    if type(list_in) != list:
        raise TypeError('Please input list.')
    else:
        list_out = []
        for i in range(1, len(list_in), 2):
            list_out.append(list_in[i])
        return list_out

display_result = pick_from_list([1, 2, 3, 4, 5])
print(display_result)
