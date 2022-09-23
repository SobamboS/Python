def counter(iterable: list | str | tuple) -> dict:
    item_dict = {}

    for item in iterable:
        if item in item_dict:
            item_dict[item] = item_dict[item] + 1
        else:
            item_dict[item] = 1

    return item_dict

print(counter("Hello"))


