import keyboard
import pyautogui
import pydirectinput
import time

if __name__ == '__main__':

    # Make sure this does not conflict with any keybinding in the game!
    buttonToStartAutotyping = 'o'



    # Beginning of program
    # Wait for user input to start typing
    keyboard.wait(buttonToStartAutotyping)

    # Open the list of commands to type
    # Read each line and create a list with each command as an element
    # Make sure to clean the list before executing program. It should look like this:

    # /spawnitem 123456
    # /spawnitem 987654
    # /spawnitem 123456
    # /spawnitem 987654

    commands = open("commandlist.txt").readlines()

    # Print to screen for debugging purposes
    print(commands)

    # Counter for keeping track of progress
    currentPosition = 1

    # Loop through all commands to type them in one-by-one
    for cmd in commands:
        
        # Strip the command of it's new line character '\n'
        cmd = cmd.strip()


        # These times are for delaying the program so the game doesn't get confused
        # Time between opening dialogue and entering command
        preCmdDelay = 0.25

        # Time between executing command and restarting the loop
        postCmdDelay = 0.5

        # If you have to open a dialogue to type, uncomment this
        # Start with dialogue closed before running program
        pydirectinput.press('enter')
        print('first enter pressed')

        # Delay by preCmdDelay seconds so the game can register
        time.sleep(preCmdDelay)

        # Type in the full command
        pyautogui.typewrite(cmd)
        print('command entered')

        # Press enter to input the command to the game
        pydirectinput.press('enter')
        print('second enter pressed')

        # Output current position in the list and add one to it for next time
        print(str(currentPosition) + ' out of ' + str(len(commands)))
        currentPosition += 1

        # Delay by postCmdDelay seconds so the game can register
        time.sleep(postCmdDelay)