#Matthew Herman and Tyler Smith
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
class Rooms(): #Tyler Smith did this
 def __init__(self, roomID):
  self.roomID=roomID
  self.connections={}
  self.items={}
 def add_items(self, items):
  self.items.update(stuff)
 def getDisc(self):
  if(self.roomID==0): #West Room
   print("Welcome to the West Room. There are some nice pictures on the walls.")
  elif(self.roomID==1): #East Room
   print("Welcome to the East Room. There are a lot of pots thrown about.")
  elif(self.roomID==2): #North Room
   print("Welcome to the North Room. You see a big door at the end of the dark hallway, it won't budge (yet?)")
  elif(self.roomID==3): #South Room
   print("Welcome to the South Room. You see a Family Crest and seal on the wall with a sword.")
  else:
   print("INVALID ROOM"); print(error);
 def connect( self, rm2, direct ):
  self.connections[direct]=rm2

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
   cmd=input(">>> ").lower(); #Gotta sanitize dem inputs
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
	W=Rooms(0);
	W.getDisc();
	cli.add('help',D.help);
	cli.add("kill",D.kill);
	cli.add("restart",D.restart);
	cli.add("west",D.west);cli.add("east",D.east);cli.add("south",D.south);cli.add("north",D.north);
	cli.start();
	r1=Room("North Room")
	r2=Room("South Room")
	r3=Room("West Room")
	r4=Room("East Room")
  #Room 1 connections
  r1.connect( r2, 'South' )
  r1.connect( r3, 'West' )
  r1.connect( r4, 'East' )
  #Room 2 connections
  r2.connect( r1, 'North' )
  r2.connect( r3, 'West' )
  r2.connect( r4, 'East' )

  #Room 3 connections
  r3.connect( r1, 'North' )
  r3.connect( r2, 'South' 
  r3.connect( r4, 'East' )

  #Room 4 connections
  r4.connect( r1, 'North' )
  r4.connect( r2, 'South' )
  r4.connect( r3, 'West' )

