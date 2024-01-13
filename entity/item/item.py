class Item:
    def __init__(self, name, description, id) -> None:
        self.name = name
        self.description = description
        self.id = id

    def __hash__(self) -> int:
        return str(self.id)