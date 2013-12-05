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

print(helpmenu);
#test=Commands();
while(gameon==True):
	#test.getCommand();
	#test.printCommand();
	#test.isValid(); #Command validation
	#print(gameon);
	cli=CLI();
	D=Player("Dave");
	cli.add('help',D.help);
	cli.start();
