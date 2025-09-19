def sort_list(data):
    # numbers: include ints and floats but exclude booleans
    numbers = sorted([
        x for x in data if (isinstance(x, (int, float)) and not isinstance(x, bool))
    ])
    # strings: sort case-insensitively
    strings = sorted([x for x in data if isinstance(x, str)], key=str.lower)
    # return numbers first, then strings
    return numbers + strings


items = [3, "apple", 1, "banana", 2]
print(sort_list(items))


