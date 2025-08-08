"""
1_basic_operations.py
Basic list operations: creation, append, insert, remove, update, search, length, clear, reverse, copy
"""

def create_list():
    return [1, 2, 3, 4]

def append_element(lst, element):
    lst.append(element)
    return lst

def insert_element(lst, index, element):
    lst.insert(index, element)
    return lst

def remove_element(lst, element):
    if element in lst:
        lst.remove(element)
    return lst

def update_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
    return lst

def search_element(lst, element):
    return element in lst

def list_length(lst):
    return len(lst)

def clear_list(lst):
    lst.clear()
    return lst

def reverse_list(lst):
    return lst[::-1]

def copy_list(lst):
    return lst.copy()

if __name__ == "__main__":
    my_list = create_list()
    print("Original:", my_list)
    print("Appended:", append_element(my_list, 5))
    print("Inserted:", insert_element(my_list, 2, 99))
    print("Removed:", remove_element(my_list, 3))
    print("Updated:", update_element(my_list, 1, 100))
    print("Searched 4:", search_element(my_list, 4))
    print("Length:", list_length(my_list))
    print("Reversed:", reverse_list(my_list))
    print("Copy:", copy_list(my_list))
    print("Cleared:", clear_list(my_list))