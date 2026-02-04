import sys


def main() -> None:

    print("=== Inventory System Analysis ===")

    inventory = {}

    for arg in sys.argv[1:]:
        name, qty = arg.split(':')
        inventory[name] = int(qty)

    total_items = sum(inventory.values())
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("=== Current Inventory ===")
    for item, qty in inventory.items():
        percentage = (qty / total_items) * 100 if total_items > 0 else 0
        print(f"  {item}: {qty} ({percentage:.2f}%)")

    print("=== Inventory Statistics ===")

    if inventory:
        max_item = max(inventory, key=inventory.get)
        min_item = min(inventory, key=inventory.get)
        print(f"Most abundant: {max_item} ({inventory[max_item]})")
        print(f"Least abundant: {min_item} ({inventory[min_item]})")

    categories = {"Moderate": {}, "Scarce": {}}
    for item, qty in inventory.items():
        if qty >= 5:
            categories["Moderate"][item] = qty
        else:
            categories["Scarce"][item] = qty

    print("=== Item Categories ===")
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    restock = [item for item, qty in inventory.items() if qty <= 1]

    print("=== Management Suggestions ===")
    if restock:
        print(f"Restock needed: {restock}")
    else:
        print("All items sufficiently stocked.")

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary Keys: {list(inventory.keys())}")
    print(f"Dictionary Values: {list(inventory.values())}")
    print(f"Sample lookup - 'potion' in inventory: {'potion' in inventory}")


if __name__ == "__main__":
    main()
