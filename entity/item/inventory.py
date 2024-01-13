from collections import Counter
from item import Item

class Inventory:
    def __init__(self):
        self.items = set()
        self.items_count = Counter()

    def add_item(self, item: Item):
        self.items.add(item)
        self.items_count[item] += 1

    def pop_item(self, item: Item):
        if item in self.items:
            self.items_count[item] -= 1
            if self.items_count[item] == 0:
                self.items.remove(item)

    def get_item_count(self, item: Item) -> int:
        return self.items_count[item]

    def has_item(self, item: Item) -> bool:
        return item in self.items

    def get_items(self) -> list:
        return list(self.items)
    
    def extend(self, other_inventory: 'Inventory'):
        self.items.update(other_inventory.items)
        self.items_count.update(other_inventory.items_count)

    def clear(self):
        self.items.clear()
        self.items_count.clear()

    def __contains__(self, item):
        return item in self.items