"""
4_array_algorithms.py
Common array algorithms: sum, average, min, max, sort, filter, deduplicate, find pairs, count
"""

def calculate_sum(lst):
    return sum(lst)

def calculate_average(lst):
    return sum(lst) / len(lst) if lst else 0

def find_min(lst):
    return min(lst)

def find_max(lst):
    return max(lst)

def sort_ascending(lst):
    return sorted(lst)

def sort_descending(lst):
    return sorted(lst, reverse=True)

def filter_even(lst):
    return [x for x in lst if x % 2 == 0]

def unique_elements(lst):
    return list(set(lst))

def count_occurrences(lst, target):
    return lst.count(target)

def find_pairs_with_sum(lst, target_sum):
    seen = set()
    pairs = []
    for num in lst:
        if target_sum - num in seen:
            pairs.append((num, target_sum - num))
        seen.add(num)
    return pairs

if __name__ == "__main__":
    data = [4, 2, 7, 2, 9, 4, 6, 8]
    print("Sum:", calculate_sum(data))
    print("Average:", calculate_average(data))
    print("Min:", find_min(data))
    print("Max:", find_max(data))
    print("Sorted:", sort_ascending(data))
    print("Sorted desc:", sort_descending(data))
    print("Even numbers:", filter_even(data))
    print("Unique:", unique_elements(data))
    print("Occurrences of 4:", count_occurrences(data, 4))
    print("Pairs with sum 10:", find_pairs_with_sum(data, 10))