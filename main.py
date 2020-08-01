import replit
import random
print('Welcome to Tic-Tac-Toe')
gameStarted = 0
grid = [["[]", "[]", "[]"], ["[]", "[]", "[]"], ["[]", "[]", "[]"]]
gamemode = "1"
selection = 0
gameFinished = 0
running = True

def aiMove():

  if(gamemode == "1"):
    pos1 = random.randrange(0,2)
    pos2 = random.randrange(0,2)
    while(grid[pos1][pos2] == "X" or grid[pos1][pos2] == "X"):
      pos1 = random.randrange(0,2)
      pos2 = random.randrange(0,2)
    return str(pos1)+","+str(pos2)


  if(gamemode == "2" or gamemode == "3"):
    pass
    
  if(gamemode == "4"):
      pass

def allFilled():
  count = 0
  for a in range(len(grid)):
    for b in len(grid[a]):
      if(grid[a][b]=="X" or grid[a][b]=="O"):
        count += 1
  if(count == 9):
    print("It's a draw!")
    return True
  else:
    return False

def drawGrid():
  print ("\a")
  for i in grid:
      print(i)

def gameOver():
  winner = whoWon()
  if(winner == 1 or winner == 2 or allFilled == True):
      return True
  else:
    return False


def whoWon():
    player1Pieces = 0
    player2Pieces = 0
    for h in range(len(grid)):
        for i in range(len(grid[h])):
            if (grid[h][i] == piece1):
                player1Pieces += 1
            elif (grid[h][i] == piece2):
                player2Pieces += 1
    if (player1Pieces >= 3):
        return 1
    elif (player2Pieces >= 3):
        return 2
    else:
        player1Pieces = 0
        player2Pieces = 0
    for h in range(len(grid)):
        for i in range(len(grid[h])):
            if (grid[i][h] == piece1):
                player1Pieces += 1
            elif (grid[i][h] == piece2):
                player2Pieces += 1
    if (player1Pieces >= 3):
        return 1
    elif (player2Pieces >= 3):
        return 2
    else:
        player1Pieces = 0
        player2Pieces = 0
    for i in range(len(grid)-1):
        if (grid[i][i] == piece1):
            player1Pieces += 1
        elif (grid[i][i] == piece2):
            player2Pieces += 2
    if (player1Pieces >= 3):
        return 1
    elif (player2Pieces >= 3):
        return 2
        
    else:
      return 0


while(running == True):
  while (gameStarted == 0):
    while(selection == 0):
      print("Please select a gamemode")
      print("1. Easy \n 2. Medium \n 3. Hard \n 4. Impossible \n 5. Play with a friend \n 0. Quit \n")
      gamemode = input()
      if(gamemode == "0"):
        exit()
      elif(int(gamemode) > 5 or int(gamemode) < 0 ):
        print('Invalid gamemode.')
      else:
        selection = 1
    

    print("Do you want to use 'X' or 'O'")
    piece = input()
    replit.clear()
    if (piece == "X"):
        player = 1
        piece1 = "X"
        piece2 = "O"

    else:
        player = 2
        piece1 = "O"
        piece2 = "X"     
    gameStarted = 1

  while (gameOver()==False):
    replit.clear()
    invalid = 1
    print("You are "+piece1)
    print('\n Your oponent is'+ piece2) 
    drawGrid();
    print("It is player " + str(player) + "'s turn.")
    while(invalid == 1):
      print('Enter X and Y cordinates like so "2,2"')
      if(gamemode == "5"):
        cords = input()
      else:
        cords = aiMove()
      if(len(cords)==3 and (0<=int(cords[0])<=2) and (0<=int(cords[2])<=2)):
        if(cords[0].isnumeric()):
          if(cords[1]==','):
            if(cords[2].isnumeric()):
              invalid = 0
              if(grid[int(cords[0])][int(cords[2])]=='[]'):
                if(player == 1):
                  print('moved player'+str(player)+'s piece')
                  grid[int(cords[0])][int(cords[2])]= piece1;
                  if(gameOver() == False):
                    player = 2
                  
                elif(player == 2):
                    print('moved player'+str(player)+'s piece')
                    grid[int(cords[0])][int(cords[2])]= piece2;
                    if(gameOver() == False):
                      player = 1
                  
              else:
                print("That space is already occupied!")
              
    else:
      invalid = 1
  drawGrid()
  print("\n Game Over: "+"Player "+ str(player)+"wins!!!")
  print("Press '1' to start a new game. \n Press '0' to exit \n")
  i = input()
  if(i == "0"):
    exit()
  else:
    grid = [["[]", "[]", "[]"], ["[]", "[]", "[]"], ["[]", "[]", "[]"]]
    replit.clear()



