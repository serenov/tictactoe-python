import os

def TheEnd():
    p = 0
    for y in range(0, 8):
        for x in range(0, 3):
            if x == 0:
                p = board[indices[y][x]]
                if p == 0:
                    break
            elif board[indices[y][x]] != p:
                break
            if x == 2: 
                os.system("cls")
                display()
                print(f"{decode(p)} is the winner")
                return True
    return False

def isLegal(x):
    if x > 8 or x < 0:
        return False
    elif board[x] == 0:
        return True
    return
def decode(id):
    if id == 2:
        return 'X'
    elif id == 1:
        return 'O'
    return ' '
    
def display():
    print(" -----------------")
    print(f"|  {decode(board[0]) }  |  {decode(board[1])}  |  {decode(board[2])}  |")
    print(" -----------------")
    print(f"|  {decode(board[3])}  |  {decode(board[4])}  |  {decode(board[5])}  |")
    print(" -----------------")
    print(f"|  {decode(board[6])}  |  {decode(board[7])}  |  {decode(board[8])}  |")
    print(" -----------------")
    return;
# x interpreted as 1, o interpreted -1
board = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
]
indices = [
    [2, 4, 6],
    [0, 1, 2],
    [0, 4, 8],
    [0, 3, 6],
    [6, 7, 8],
    [2, 5, 8],
    [3, 4, 5],
    [1, 4, 7]
]

isXTurn = True
count = 0;
while(not(TheEnd())):
    os.system("cls")
    display()
    if isXTurn:
        print("X's turn...")
    else:
        print("O's turn")
    x = int(input("Enter a position: ")) - 1
    if isLegal(x) == True:
        if isXTurn == True:
            board[x] = 2;
            isXTurn = False
        else:
            board[x] = 1;
            isXTurn = True
        count += 1
    else:
        print("Select a valid position")
    if count == 9: 
        os.system("cls")
        display()
        print("Draw!!!")
        break;
