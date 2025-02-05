"""
This is a module docstring
"""
#!/usr/bin/env python3


class VerboseList(list):
    """
    This is a class docstring
    """

    def __init__(self, items=[]):
        super().__init__(items)

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, new_items):
        super().extend(new_items)
        print(f"Extended the list with [{len(new_items)}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
