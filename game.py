#PyZork
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




