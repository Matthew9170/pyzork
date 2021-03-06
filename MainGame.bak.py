pyzork/MainGame.py                                                                                  0000644 0001750 0000144 00000006505 12251374265 011376                                                                                                                                                                               0000000 0000000                                                                                                                                                                        #Matthew Herman and Tyler Smith
#Python Implementation of Zork
#November 2013 - December 2013
#Benedetto


'''NOTE'''
	#Tyler is working on the rooms code and maps code

'''Global Variables'''
error="I'm sorry Dave, I can't let you do that.";
helpmenu=(
	"***********************************************************************************\n"+
	"*****HELP MENU*****\n"+
	"This is the help menu.\n"+
	"All commands are one letter except for taking items.\n"+
	"Some commands are as follows,\n"+
	"'g [DIRECTION]' This command will bring you to that room.\n"+
	"'t [ITEM]' This command will remove the item from the floor and place it in your backpack.\n"+
	"'d [ITEM]' This command will drop the item from your backpack and it will be gone for good.\n"+
	"'r' This will restart the room.\n"+
	"'l' Will print the description of the room.\n"+
	"'e' This will exit the game.\n"+
	"'h' This will print this message out again.\n\n"+
	"**********************************************************************************\n"+
	"Have fun, don't break things.")
command=""; #Must assign it the global tag in each function that needs it
gameon=True;
'''Set up the skeleton for the rooms'''
class Rooms():
	def __init__(self, desc):
		self.description=desc;
		self.connections={};
		self.items={};
	def add_items(self, items):
		pass
'''
class Commands():
	commandvalid=True; #All commands are true unless specified
	def getCommand(self):
		global command;
		command=input(">>> ");
		return command;
	def printCommand(self):
		print(command);
	def isValid(self):
		commandtest=command[:1];
		if(commandtest=="g" or commandtest=="t" or commandtest=="d" or commandtest=="r" or commandtest=="l" or commandtest=="e" or commandtest=="h"):
			print("Valid Command");
			if(commandtest=="e"):
				global gameon;
				gameon=False;
		else:
			print(error);
			return;
		#print(commandtest);
'''#That would have worked too.
'''str getCommand():
	command=input(">>> ");
	if(command=="h"):
		print(helpmenu);
''' #Python doesn't have objectfuctions sadface

class CLI():
 def __init__(self):
  self.cmds={};
 def add(self, cmd, action):
  self.cmds[cmd]=action;
 def run(self,cmd,params=[]):
  try:
   self.cmds[cmd](params);
  except Exception as e:
   print(type(e),':',e);
 def start(self):
  while(1):
   cmd=input(">>> ");
   stuff=cmd.split(' ');
   if(stuff[0] in ['exit','quit','leave','42']):
    print("Leaving DA BEST ZORK EVA");
    break;
   if(len(stuff)>1):
    self.run(stuff[0],stuff[1:]);
   else:
    self.run(stuff[0],[]);
class Player():
	def __init__(self,name):
		self.name=name;
	def help(self, params):
		print(helpmenu);
	def restart(self, params):
		print(mainstring);
	def kill(self, params):
		print(error);
	def west(self, params):
		print("Going to West Room");
		#GOTO room 0;
	def north(self, params):
		print("Going to the North Room");
		#GOTO room 1
	def east(self, params):
		print("Going to the East Room");
		#GOTO room 2
	def south(self, params):
		print("Going to the South Room");
		#GOTO room 3

print(helpmenu);
#test=Commands();
if __name__=='__main__':
	#test.getCommand();
	#test.printCommand();
	#test.isValid(); #Command validation
	#print(gameon);
	cli=CLI();
	D=Player("Dave");
	cli.add('help',D.help);
	cli.add("kill",D.kill);
	cli.add("restart",D.restart);
	cli.add("west",D.west);cli.add("east",D.east);cli.add("south",D.south);cli.add("north",D.north);
	cli.start();
                                                                                                                                                                                           pyzork/README                                                                                       0000644 0001750 0000144 00000000013 12250131435 010177                                                                                                                                                                               0000000 0000000                                                                                                                                                                        HelloWorld
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     pyzork/game.py                                                                                      0000644 0001750 0000144 00000004353 12247671301 010624                                                                                                                                                                               0000000 0000000                                                                                                                                                                        #PyZork
'''
4 rooms
   NNNNNNNNNN	
WWWWWWW  EEEEEEE
   SSSSSSSSSS
go east, west, north, south

Rooms will have an inventory
	the inverntory will hold items and stuff



'''
class Rooms():
	Error="I'm sorry Dave, I can't let you do that.";
	cangoWest=True;
	cangoEast=True;
	cangoNorth=True;
	cangoSouth=True;
	roomID=-1;
	descr=["Welcome to the west room. There are some nice pictures on the walls."
,"Welcome to the east room. There are a lot of pots thrown about."
,"Welcome to the north room. You see a big door at the end of the dark hallway, it won't budge."
,"Welcome to the south room. You see the family crest and seal."]
	Efloor=[];Sfloor=[];Wfloor=[];Nfloor=[];floor=[];
'''
def WestRoom():
	room=Rooms();
	room.roomID=0;
	print(room.descr[room.roomID])
	room.floor.append("Gun")
	print(room.floor[0])
'''
#West room = 0
#East room = 1
#North room = 2
#South room = 3
#Main room = 4
class Player():
	CurrentRoom=-1
	backpack=[];



currentRoom=0;
gameon=True;
class game():
	#Setup the rooms
	WestRoom=Rooms();
	WestRoom.roomID=0;
	WestRoom.cangoWest=False;	
	WestRoom.floor.append("Bracer");
	WestRoom.floor.append("Picture");
	
	EastRoom=Rooms();
	EastRoom.roomID=1;
	EastRoom.cangoEast=False;
	EastRoom.floor.append("Master Sword");
	EastRoom.floor.append("Pot");

	NorthRoom=Rooms();
	NorthRoom.roomID=2;
	NorthRoom.cangoNorth=False;
	NorthRoom.floor.append("Golden Roshling");
	
	SouthRoom=Rooms();
	SouthRoom.roomID=3;
	SouthRoom.cangoSouth=False;
	SouthRoom.Sfloor.append("Key");


	#DEBUG
	print(NorthRoom.roomID, NorthRoom.descr[NorthRoom.roomID]);
	print(NorthRoom.floor[0]);NorthRoom.floor.pop(0);
	print(EastRoom.roomID, EastRoom.descr[EastRoom.roomID]);
	print(NorthRoom.floor[0]);
	print("\n"*10);
	'''
	if player.command=="Go east":
		player.currentRoom=1;
		//CALL ROOM STUFFS
	if player.command=="Take $OBJECT":
		//Search for item in current room's floor
		//If item found
		player.backpack.append($OBJECT);
		$ROOM.floor.remove($OBJECT);
		//If object not found
		print($ROOM.error);
	if player.command=="Look":
		//CALL ROOM STUFF as if entering room again
	'''
	while(gameon==True):
		Dave=Player();
		Dave.CurrentRoom=0;
		if(Dave.CurrentRoom==-1):
			gameon==False;
			print("Game Over");
		if(Dave.CurrentRoom==0):
			WestRoom.descr[0];
game();




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     