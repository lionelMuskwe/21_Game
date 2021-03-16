import random
sticks = 21 # defines the number of sticks to be used in the game

def computerPlayMove():
    global sticks
    if sticks % 4 > 0:
        cpuSticks = sticks % 4
    else:
        cpuSticks = random.randint(1,3)

    sticks -= cpuSticks
    print("CPU Removed: {0} stick(s)".format(cpuSticks))
    
def playerPlayMove():
    global sticks
    while True:
        playerSticks = input("Sticks to remove: ")
        if playerSticks.isdigit():
            playerSticks = int(playerSticks)
            if  playerSticks > 0 and playerSticks <= 3:
                sticks -= playerSticks
                print("Player Removed: {0} stick(s)".format(playerSticks))
                break
            else:
                print("Well done for choosing a number, but make it [1, 2 or 3]")
        else:
            print("You need to enter a number between [1] and [3]")

def gameOver():
    print("Game Over")

def gameLoop():
    while sticks >= 0:
        if sticks > 0:
            print("\t\t\t\t Sticks left : " + str(sticks))
            playerPlayMove()
            if sticks > 0:
                print("\t\t\t\t Sticks left : " + str(sticks))
                computerPlayMove()
            else:
                print("Player wins")
                gameOver()
                break
        else:
            print("Computer Wins")
            gameOver()
            break

gameLoop()