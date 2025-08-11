
## List slicing and indexing techniques: slice, step, negative indices, sublists, combinations


def get_element(lst, index):
    return lst[index]

def get_last_element(lst):
    return lst[-1]

def get_sublist(lst, start, end):
    return lst[start:end]

def get_every_second(lst):
    return lst[::2]

def get_reversed(lst):
    return lst[::-1]

def get_middle_section(lst):
    mid = len(lst) // 2
    return lst[mid - 1:mid + 2]

def exclude_edges(lst):
    return lst[1:-1]

def slice_with_step(lst, step):
    return lst[::step]

def reverse_every_third(lst):
    return lst[::-3]

def custom_slice(lst, start, end, step):
    return lst[start:end:step]

if __name__ == "__main__":
    sample = [10, 20, 30, 40, 50, 60, 70]
    print("Element at 2:", get_element(sample, 2))
    print("Last element:", get_last_element(sample))
    print("Sublist (1:4):", get_sublist(sample, 1, 4))
    print("Every second:", get_every_second(sample))
    print("Reversed:", get_reversed(sample))
    print("Middle section:", get_middle_section(sample))
    print("Exclude edges:", exclude_edges(sample))
    print("Step 3:", slice_with_step(sample, 3))
    print("Reverse every third:", reverse_every_third(sample))
    print("Custom slice (1:6:2):", custom_slice(sample, 1, 6, 2))
