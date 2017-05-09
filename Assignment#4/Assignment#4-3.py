__author__ = 'w0293156'
#import function
import csv
#Function to read a map and store it in a two dimensional list and then return to list.
def readmap(fileName):
    myCSVFile = None
    try:
        with open(fileName,"r") as myCSVFile:
            dataFromFile = csv.reader(myCSVFile,delimiter="\n")
            list_map = []
            for row in dataFromFile:
                for value in row:
                    list_map.append(value)
            for i in range(len(list_map)):
                list_map[i] = list_map[i].split(',')
        return list_map
#Display error message
    except IOError:
        print("IOError - cannot write a file!")
    except PermissionError:
        print("PermissionErro - cannot write a file.")
    except:
        print("Error occurred")
    finally:
        myCSVFile.close()
#Function to print board status
def print_board(board):
    print('\n    ', end="")
    for i in range(10):
        print(str(i)+ ' ', end="")
    print('\n   ----------------------')
    for i in range(len(board)):
        print(str(i) +' | '+ " ".join(board[i]))

#Function to play battleship
def play_battleship(list_map,numberOfMissiles,numberOfBattleships):
    win = False
    board = []
    for x in range(10):
        board.append([" "] * 10)
    print_board(board)

    sunk_battleship = 0
    turn = 0
    while turn < numberOfMissiles:
        guess_location = input("\nChoose your target <Ex: 1,2>: ")
        if len(guess_location) != 3:
            print("Enter valid location..")
            continue
        elif guess_location[0].isdigit() == False or guess_location[2].isdigit() == False or guess_location[1] != ',':
            print("Enter valid location..")
            continue
        guess_row = int(guess_location[0])
        guess_col = int(guess_location[2])

        if list_map[guess_row][guess_col] == '1':
            if board[guess_row][guess_col] == "O": # Check if already guessed or not, which is correct.
                print("You guessed that one already.")
                continue
            else:
                sunk_battleship += 1
                print("\nHit! You sunk my battleship(total: {0})\n"
                      "{1} opportunity(ies) left".format(str(sunk_battleship),str(numberOfMissiles-(turn+1))))
                board[guess_row][guess_col] = "O"
                # Check if the number of battleship equal to the number of sunk battleship
                if sunk_battleship == numberOfBattleships:
                    print_board(board)
                    win = True
                    break
        else:
            # Check if it is in the ocean or not
            if (guess_row < 0 or guess_row > 30) or (guess_col < 0 or guess_col > 30):
                print("Oops, that's not even in the ocean.")
                continue
            # Check if already guessed or not, which is not correct.
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
                continue
            else:
                board[guess_row][guess_col] = "X"
                print("\nMiss! {0} opportunity(ies) left\n"
                      "Total sunk battleship until now: {1}".format(str(numberOfMissiles-(turn+1)),str(sunk_battleship)))
        print_board(board) # Update board display
        turn += 1
    return win

#Run the files
print("Let's play Battleship!")

#Define variables
numberOfMissiles = 30
numberOfBattleships = 17

#Read a map and store it in a two dimensional list and then return to list.
fileName = "Assignment#4-3_Map.txt"
list_map = readmap(fileName)

#Play and print the result
if play_battleship(list_map,numberOfMissiles,numberOfBattleships):
    print('\nCongratulations! You won! You sunk all my battleships.\nGame Over')
else:
    print('\nYou lose.\nGame Over.')