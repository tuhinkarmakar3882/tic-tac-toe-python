class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def __str__(self):
        return self.name
