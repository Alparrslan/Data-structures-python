"""
5_array_use_cases.py
Real-life list use cases: score calculation, name filtering, inventory updates, matching items
"""

def average_score(scores):
    return round(sum(scores) / len(scores), 2)

def filter_passed(scores, threshold=60):
    return [score for score in scores if score >= threshold]

def remove_duplicates(names):
    return list(dict.fromkeys(names))

def match_names(list1, list2):
    return list(set(list1) & set(list2))

def get_top_n(scores, n=3):
    return sorted(scores, reverse=True)[:n]

def update_inventory(inventory, sold_items):
    for item in sold_items:
        if item in inventory:
            inventory.remove(item)
    return inventory

def calculate_total_price(prices):
    return round(sum(prices), 2)

def get_items_starting_with(items, letter):
    return [item for item in items if item.startswith(letter)]

def add_new_items(inventory, new_items):
    inventory.extend(new_items)
    return inventory

def product_search(products, keyword):
    return [p for p in products if keyword.lower() in p.lower()]

if __name__ == "__main__":
    scores = [70, 85, 90, 55, 60]
    names1 = ["Alice", "Bob", "Charlie"]
    names2 = ["Charlie", "David", "Alice"]
    inventory = ["apple", "banana", "carrot", "banana"]
    print("Average score:", average_score(scores))
    print("Passed:", filter_passed(scores))
    print("No duplicates:", remove_duplicates(inventory))
    print("Matched names:", match_names(names1, names2))
    print("Top 3 scores:", get_top_n(scores))
    print("Updated inventory:", update_inventory(inventory, ["banana"]))
    print("Total price:", calculate_total_price([10.5, 5.75, 3.20]))
    print("Starts with 'a':", get_items_starting_with(inventory, "a"))
    print("Inventory + new:", add_new_items(inventory, ["orange", "grape"]))
    print("Search products:", product_search(["Milk", "Dark Chocolate", "Almond Milk"], "milk"))