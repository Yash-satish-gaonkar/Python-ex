def unique_sort_ele(lst):
    tpl = tuple(lst)
    unique_set = set(tpl)
    return sorted(unique_set)

print(unique_sort_ele(["apple", "banana", "apple", "mango"]))
