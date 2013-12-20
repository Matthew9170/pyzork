#import imp
#imp.reload(module)
import time
import sys


def typ(s):
	for letter in s:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.02)


class Item:  # Item Class Definition
	def __init__(self, name, description, catagory="misc",
		attack_bonus=0, heal=0):
		self.name = name
		self.catagory = catagory
		self.attack_bonus = attack_bonus
		self.heal = heal
		self.description = description

	def change_name(self, item, name):
		self.name = name

	def change_catagory(self, item, catagory):
		self.catagory = catagory

	def change_attack_bonus(self, item, attack_bonus):
		self.attack_bonus = attack_bonus

	def change_heal(self, item, heal):
		self.heal = heal

	def add_description(self, item, description):
		self.description = description


class System:  # System Class Definition
	def __init__(self):	 # Constructor
		pass


class Room:  # Room Class Definition
	def __init__(self, n, loot=[], d="", adj={}, npcs={}):
		self.name = n
		self.description = d
		self.item_description = ""
		self.loot = []
		self.adjacent_rooms = {}
		self.adjacent_rooms.update(adj)
		self.npcs = {}
		self.npcs.update(npcs)

	def add_adjacent_rooms(self, rm, direction):
		self.adjacent_rooms.update({direction: rm})
		opp = {"n": "s", "e": "w", "s": "n", "w": "e"}
		if opp[direction] not in rm.adjacent_rooms:
			rm.adjacent_rooms[opp[direction]] = self

	def get_adjacent_rooms(self):
		string = ""
		for key in self.adjacent_rooms:
			string += key + ": " + self.adjacent_rooms[key].name +\
				"; "
		return string

	def add_loot(self, item):
		self.loot.append(item)

	def add_description(self, description):
		self.description = description

	def describe(self):
		if len(self.loot) > 0:
			typ(self.description + self.item_description)
		else:
			typ(self.description)

	def get_loot(self):
		string = ""
		for x in range(len(self.loot)):
			if x == len(self.loot):
				string += str(self.loot[x].name) + ", "
			else:
				string += str(self.loot[x].name)
		return string


class Player:  # Player Class Definition
	def __init__(self, n="Anon"):
		self.name = n
		self.inv = []
		self.location = "start_area"

	def go(self, direction):
		if direction == ['north'] and "n" \
		in self.location.adjacent_rooms:
			self.location = self.location.adjacent_rooms["n"]
			typ(self.location.description)
		elif direction == ['south'] and "s" \
		in self.location.adjacent_rooms:
			self.location = self.location.adjacent_rooms["s"]
			typ(self.location.description)
		elif direction == ['east'] and "e" \
		in self.location.adjacent_rooms:
			self.location = self.location.adjacent_rooms["e"]
			typ(self.location.description)
		elif direction == ['west'] and "w" \
		in self.location.adjacent_rooms:
			self.location = self.location.adjacent_rooms["w"]
			typ(self.location.description)
		else:
			typ("That is not a valid direction")

	def look(self, thing):
		typ(self.location.description)

	def take(self, item):
		if item in self.location.loot:
			self.inv.append(item)
			self.location.loot.remove(item)
			self.location.description


class CLI:
	def __init__(self):
		self.cmds = {}

	def add_cmd(self, cmd, action):
		self.cmds[cmd] = action

	def run_cmd(self, cmd, params=[]):
		try:
			self.cmds[cmd](params)
		except Exception as e:
			#print(type(e), ':', e)
			typ(str(type(e)) + ':' + str(e))

	def start(self):
		while(1):
			cmd = input("\n> ")
			# Tokenize
			tokens = cmd.split(' ')
			if tokens[0] in ['exit', 'quit', 'bye']:
				typ("Bye")
				break
			# Process
			if len(tokens) > 1:
				self.run_cmd(tokens[0], tokens[1:])
			else:
				self.run_cmd(tokens[0], [])


def main():
	# Item(name, description, catagory, attack_bonus, heal

	# Get the player's name, if not inputted, assume "Anon"
	n = input("What is your name?\n> ")
	if n == "" or n == " ":
		char = Player()
	else:
		char = Player(n)
	typ("\nYou're " + char.name + "?\n")
	time.sleep(1)
	typ("Well even if you aren't that's your name now. \n")
	time.sleep(1.5)
	typ("Deal with it. \n\n")
	time.sleep(2)
	#print("\n")

	# Item Declarations
	Guide = Item("the Guide", "A guide to this game", "info")
	water_bottle = Item("a water bottle", "A bottle of water", "heal", -5, 10)

	# Room Declarations
	start_area = Room("start_area")
	start_area.add_loot(Guide)
	start_area.add_description("You are in a grassy field. ")
	start_area.item_description = "You see " + (start_area.get_loot()) + ".\n"
	start_area.add_description("You are in a grassy field. You see " +
		(start_area.get_loot()) + ".\n")

	N = Room("N")
	N.add_loot(water_bottle)
	N.add_description("You are in a grassy field. You see " +
		(N.get_loot()) + ".\n")

	S = Room("S")
	S.add_loot(water_bottle)
	S.add_description("You stand on a large hill. You see " +
		(S.get_loot()) + ".")

	# Set adjacencies
	start_area.add_adjacent_rooms(N, "n")
	start_area.add_adjacent_rooms(S, "s")

	# Add Commands
	cli = CLI()
	cli.add_cmd("go", char.go)
	cli.add_cmd("look", char.look)
	#cli.add_cmd("get", char.get)

	# ***TESTING***
	# Start playing
	char.location = start_area
	typ(start_area.description)
	time.sleep(2)

	# PLAY
	cli.start()
main()
