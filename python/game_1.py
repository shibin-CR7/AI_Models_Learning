# Import the required modules
import random

# Define the game constants
GAME_TITLE = "The Cursed Temple"
GAME_DESCRIPTION = "You are an adventurer seeking fortune and glory in the ancient temple."
GAME_OVER_MESSAGE = "Game Over! You died."

# Define the player attributes
class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.health = 100
        self.gold = 0
        self.inventory = []

    def is_alive(self):
        return self.health > 0

# Define the game rooms
class Room:
    def __init__(self, name, description, items=None):sha
        self.name = name
        self.description = description
        self.items = items if items else []

# Define the game items
class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

# Define the game actions
class Action:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def perform(self, player, room):
        pass

class MoveAction(Action):
    def __init__(self, direction):
        super().__init__("Move", f"Move {direction}")
        self.direction = direction

    def perform(self, player, room):
        if self.direction == "north":
            room = temple.north_room
        elif self.direction == "south":
            room = temple.south_room
        elif self.direction == "east":
            room = temple.east_room
        elif self.direction == "west":
            room = temple.west_room
        print(f"You moved to the {room.name}.")
        return room

class TakeAction(Action):
    def __init__(self, item):
        super().__init__("Take", f"Take {item.name}")
        self.item = item

    def perform(self, player, room):
        if self.item in room.items:
            player.inventory.append(self.item)
            room.items.remove(self.item)
            print(f"You took the {self.item.name}.")
        else:
            print(f"There is no {self.item.name} in the room.")

class UseAction(Action):
    def __init__(self, item):
        super().__init__("Use", f"Use {item.name}")
        self.item = item

    def perform(self, player, room):
        if self.item in player.inventory:
            player.health += self.item.value
            player.inventory.remove(self.item)
            print(f"You used the {self.item.name}.")
        else:
            print(f"You don't have the {self.item.name}.")

# Define the game temple
class Temple:
    def __init__(self):
        self.north_room = Room("North Room", "A dark and mysterious room.")
        self.south_room = Room("South Room", "A room filled with treasure.")
        self.east_room = Room("East Room", "A room with a hidden door.")
        self.west_room = Room("West Room", "A room with a secret passage.")
        self.current_room = self.north_room

    def move(self, direction):
        if direction == "north":
            self.current_room = self.north_room
        elif direction == "south":
            self.current_room = self.south_room
        elif direction == "east":
            self.current_room = self.east_room
        elif direction == "west":
            self.current_room = self.west_room

# Create the game items
sword = Item("Sword", "A sharp sword.", 10)
shield = Item("Shield", "A sturdy shield.", 5)
key = Item("Key", "A key to unlock the treasure.", 0)

# Create the game rooms
temple = Temple()
temple.north_room.items.append(sword)
temple.south_room.items.append(shield)
temple.east_room.items.append(key)

# Create the game player
player = Player()

# Create the game actions
move_north = MoveAction("north")
move_south = MoveAction("south")
move_east = MoveAction("east")
move_west = MoveAction("west")
take_sword = TakeAction(sword)
take_shield = TakeAction(shield)
take_key = TakeAction(key)
use_sword = UseAction(sword)
use_shield = UseAction(shield)

# Game loop
while player.is_alive():
    print(f"\n{temple.current_room.name}\n{temple.current_room.description}")
    print("Actions:")
    print("1. Move North")
    print("2. Move South")
    print("3. Move East")
    print("4. Move West")
    print("5. Take Sword")
    print("6. Take Shield")
    print("7. Take Key")
    print("8. Use Sword")
    print("9. Use Shield")
    action = input("Choose an action: ")
    if action == "1":
        temple.move("north")
    elif action == "2":
        temple.move("south")
    elif action == "3":
        temple.move("east")
    elif action == "4":
        temple.move("west")
    elif action == "5":
        take_sword.perform(player, temple.current_room)
    elif action == "6":
        take_shield.perform(player, temple.current_room)
    elif action == "7":
        take_key.perform(player, temple.current_room)
    elif action == "8":
        use_sword.perform(player, temple.current_room)
    elif action == "9":
        use_shield.perform(player, temple.current_room)
    else:
        print("Invalid action.")

    # Check for game over
    if player.health <= 0:
        print(GAME_OVER_MESSAGE)
        break

# Game over
print("Thanks for playing!")