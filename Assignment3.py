def emptyList_XO():
  tmp_lst = []
  for i in range(9):
    tmp_lst.append(' ')
  return tmp_lst
def printBoard(xoList):
  print(xoList[0], "|",xoList[1], "|", xoList[2])
  print("----------")
  print(xoList[3], "|",xoList[4], "|", xoList[5])
  print("----------")
  print(xoList[6], "|",xoList[7], "|", xoList[8])
import random 
def whoWillGoFirst():
  player = random.randint(0,1)
  if player == 0:
    print('player A | O will go first')
  else:
    print('player B | X will go first')
  return player 
def takeInput(player,xoList):
  print("Hey player, ",player )
  flag = 0 
  while flag ==0:
    pos = int(input("Enter the position in between [ 0 to 8] - "))
    if pos>= 0 and pos <= 8:
      if xoList[pos] == ' ':
        print("valid input")
        if player == 0:
          xoList[pos] = 'O'
        else:
          xoList[pos] = 'X'
        return xoList 
        flag = 1
      else:
        print("please enter again, its occupied")
        flag = 0 
    else:
      print("please give valid input again ")
      flag = 0 
def checkWin(xolist):
  flag = 0 
  print(xolist)
  for i in range(9):
    if xolist[i] == ' ':
      flag = 1
  
  if (xolist[0] =='O' and xolist[1] == 'O'  and xolist[2] == 'O') or (xolist[3] =='O' and xolist[4] == 'O'  and xolist[5] == 'O')  or (xolist[6] =='O' and xolist[7] == 'O'  and xolist[8] == 'O') or (xolist[0] =='O' and xolist[3] == 'O'  and xolist[6] == 'O') or (xolist[1] =='O' and xolist[4] == 'O'  and xolist[7] == 'O')  or (xolist[2] =='O' and xolist[5] == 'O'  and xolist[8] == 'O') or (xolist[0] =='O' and xolist[4] == 'O'  and xolist[8] == 'O') or (xolist[6] =='O' and xolist[4] == 'O'  and xolist[2] == 'O'): 
    print('Player A is winner ')
    return 0
  elif (xolist[0] =='X' and xolist[1] == 'X'  and xolist[2] == 'X') or (xolist[3] =='X' and xolist[4] == 'X'  and xolist[5] == 'X')  or (xolist[6] =='X' and xolist[7] == 'X'  and xolist[8] == 'X') or (xolist[0] =='X' and xolist[3] == 'X'  and xolist[6] == 'X') or (xolist[1] =='X' and xolist[4] == 'X'  and xolist[7] == 'X') or (xolist[2] =='X' and xolist[5] == 'X'  and xolist[8] == 'X') or (xolist[0] =='X' and xolist[4] == 'X'  and xolist[8] == 'X') or (xolist[6] =='X' and xolist[4] == 'X'  and xolist[2] == 'X'): 
    print('Player B is winner ')
    return 1 
  elif flag == 1:
    return -1
  else:
    return 2
XO_list = emptyList_XO()
printBoard(XO_list)
play = whoWillGoFirst()
ScoreA = 0 
ScoreB = 0 

gameStatus = 0
chance = 0 

while gameStatus == 0:
  if play == 0:
    XO_list = takeInput(0,XO_list)
    printBoard(XO_list)
    winStat = checkWin(XO_list)
    play = 1
  else:
    XO_list = takeInput(1,XO_list)
    printBoard(XO_list)
    winStat = checkWin(XO_list)
    play = 0
  
  if winStat == 0 or winStat == 1 or winStat == 2:
    gameStatus = 1
    print('win - ', winStat)
  else:
    gamestatus = 0 
