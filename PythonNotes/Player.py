class Player:
    # In python , some default parameter value is mutable , such as list or dictionary
    # So Player Alice and Player Bob sharing the same list
    def __init__(self , name , items = []):
        self.name = name
        self.items = items

p1 = Player("Alice")
p2 = Player("Bob")
p3 = Player("Charles", ["sword"])

p1.items.append("armor")
p2.items.append("sword")

print(p1.items)

# Correct answer
# Set it to None
class Player:
    def __init__(self , name , items = None):
        self.name = name
        if items is None:
            self.items = []
        else:
            self.items = items

p1 = Player("Alice")
p2 = Player("Bob")
p3 = Player("Charles", ["sword"])

p1.items.append("armor")
p2.items.append("sword")

print(p1.items)

