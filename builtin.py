# Base player classes

class Player:
    def __init__(self):
        self.hp = 100
        self.xp = 0
        self.name = ''

    def __str__(self):
        return self.name

# Base node classes

class Node:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def on_select(self):
        print(self.desc)

    def __str__(self):
        return self.title


# Location behaves exactly like a Node
class Location(Node):
    pass


# Actions include the player for reference (augment player attributes)
class Action(Node):
    def __init__(self, title, desc, player):
        self.player = player
        super().__init__(title, desc)

    def on_select(self):
        super().on_select()



