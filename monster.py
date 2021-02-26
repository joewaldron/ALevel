import random

class Item:
    def __init__(self, type):
        self.Type = type
        self.Hidden = False
        self.X = 0
        self.Y = 0

    def SetLocation(self,x,y):
        self.X = x
        self.Y = y

    def GetX(self):
        return self.X

    def GetY(self):
        return self.Y

    def GetType(self):
        return self.Type

    def GetTypeSymbol(self):
        Symbol = "."
        if self.Type == "Player":
            Symbol = "*"
        elif self.Type == "Monster":
            Symbol = "M"
        elif self.Type == "Potion":
            Symbol = "P"
        elif self.Type == "Trap":
            Symbol = "T"
        return Symbol

    def SetHidden(self,state):
        self.Hidden = state

    def GetHidden(self):
        return self.Hidden

class Cavern:
    Grid = []
    def __init__(self):
        for i in range(6):
            self.Grid.append([])
            for j in range(7):
                self.Grid[i].append(Item("Empty"))

    def GetSquare(self, Row, Column):
        currentSquare = self.Grid[Row][Column]
        if currentSquare.GetHidden():
            return '.'
        else:
            return currentSquare.GetTypeSymbol()

    def HideObject(self,newItem):
        newX = 0
        newY = 0
        while self.Grid[newY][newX].GetType() != "Empty":
            newX = random.randint(0,6)
            newY = random.randint(0,5)
        self.Grid[newY][newX] = newItem
        newItem.SetHidden(True)
        newItem.SetLocation(newX,newY)

    def Move(self,item_to_move,direction):
        global monster_awake
        currX = oldX = item_to_move.GetX()
        currY = oldY = item_to_move.GetY()
        if direction == "N" and currY != 0:
                currY -= 1
        elif direction == "S" and currY != 5:
            currY += 1
        elif direction == "W" and currX != 0:
            currX -= 1
        elif direction == "E" and currX != 6:
            currX += 1
        temp = self.Grid[currY][currX]
        #optional – check if temp is a special square
        if temp.GetType() == "Trap" and item_to_move.GetType() == "Player":
            temp.SetHidden(False)
            monster_awake = True
            print("Watch out! You found a trap. The monster wakes...")
        if temp.GetType() == "Monster" or (temp.GetType() == "Player" and item_to_move.GetType() == "Monster"):
            temp.SetHidden(False)
            print("Eaten by the monster! Game Over.")
            return False
        if temp.GetType() == "Potion" and item_to_move.GetType() == "Player":
            temp.SetHidden(False)
            print("You found the Styxian Potion! You win.")
            return False

        self.Grid[currY][currX] = item_to_move
        self.Grid[oldY][oldX] = temp
        item_to_move.SetLocation(currX,currY)
        temp.SetLocation(oldX,oldY)
        return True

def DisplayGrid():
    global Cave1
    for i in range(6):
        currentLine = ""
        for j in range(7):
            currentLine += Cave1.GetSquare(i,j)
        print(currentLine)

def MoveMonster():
    global Player,Monster,Cave1,Game
    playerX = Player.GetX()
    playerY = Player.GetY()
    monsterX = Monster.GetX()
    monsterY = Monster.GetY()
    direction = ""
    turns = 2
    while (playerX != monsterX or playerY != monsterY) and turns > 0 and Game:
        if playerX < monsterX:
            direction = "W"
        elif playerX > monsterX:
            direction = "E"
        if playerY < monsterY:
            direction = "N"
        elif playerY > monsterY:
            direction = "S"
        Game = Cave1.Move(Monster,direction)
        turns -= 1
        playerX = Player.GetX()
        playerY = Player.GetY()
        monsterX = Monster.GetX()
        monsterY = Monster.GetY()

play = True
while play:
    Cave1 = Cavern() 	# instantiate object
    Game = True
    monster_awake = False
    Potion = Item("Potion") 	# create items
    Trap1 = Item("Trap")
    Trap2 = Item("Trap")
    Monster = Item("Monster")
    Player = Item("Player")
    Cave1.Grid[0][0] = Player 	# set player starting location
    Player.SetLocation(0,0)	# hide items
    Cave1.HideObject(Potion)
    Cave1.HideObject(Trap1)
    Cave1.HideObject(Trap2)
    Cave1.HideObject(Monster)
    print("Welcome to the game of Monster!")
    print("The aim of the game is to find the Styxian potion before the monster finds you...")
    DisplayGrid() 	# output grid squares

    while Game:
        Direction = input("Direction N,E,S,W: ").upper()
        Game = Cave1.Move(Player, Direction)	# user to input location to move
        if monster_awake:
            Monster.SetHidden(False)
            MoveMonster()
        DisplayGrid()

    choice = input("Would you like to play again? Y/N ").upper()
    if choice == "N":
        play = False
