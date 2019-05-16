NBR = 12
myList = [0 for i in range(NBR)]
def initiatePlayers(mylist):
    count = len(mylist) // 3
    for i in range(len(myList)):
        if i < count:
            myList[i] = 1;
        elif i < count * 3 and i >= count * 2:
            myList[i] = 2
def displayList(mylist):
    for i in range(len(myList)):
        if i >= 9:
            print(' ', end='')
        if myList[i] == 1:
            print("x ", end='')
        elif myList[i] == 2:
            print("o ", end='')
        else:
            print(". ", end='')
    print('')
    for i in range(len(myList)):
        print(str(i + 1) + " ", end='')
    print('')
def move(list, player, pawn):
    direction = 1 if player == 1 else -1
    for i in range(len(list)):
        if i == pawn and list[i] == player:
            if list[i + direction] == 0:
                list[i], list[i + direction] = list[i + direction], list[i]
                return True
            if list[i + direction] !=0 and list[i + 2*direction]==0:
                list[i], list[i + 2*direction] = list[i + 2*direction], list[i]
                return True
    return False
initiatePlayers(myList)
userInput = ""
currentPlayer = 1
continueGame = True
while continueGame:
    displayList(myList)
    userInput = input("Player " + str(currentPlayer) + " :")
    if userInput == "STOP":
        continueGame = False
        break;
    result = move(myList, currentPlayer, int(userInput) - 1)
    if result:
        currentPlayer = 2 if currentPlayer == 1 else 1
