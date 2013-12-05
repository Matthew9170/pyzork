#Matthew Herman and Tyler Smith
#Python Implementation of Zork
#November 2013 - December 2013
#Benedetto
'''Global Variables'''
error="I'm sorry Dave, I can't let you do that.";
helpmenu=("*****HELP MENU*****\n"+
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
print(helpmenu);
test=Commands();
while(gameon==True):
	test.getCommand();
	test.printCommand();
	#test.isValid(); #Command validation
	print(gameon);
