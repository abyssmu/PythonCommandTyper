## Introduction

This is a script meant to aid achievement hunters in games. It's purpose is to take a list of commands and input them one-by-one. It was specifically designed for Starbound, but should work with just about anything.

The setup for this can take a little bit of time (10 to 20 minutes), but it is well worth it. For instance, Starbound has an [achievement](https://www.trueachievements.com/a317031/armour-aficionado-achievement) to collect 210 unique armor pieces. Along with several others of considerable length. Could you imagine typing in all of that...?

## Installation

To use this, you will need to have Python 3 installed. Any version should do as the functions are not complicated. Additionally, you will need `pyautogui`, `pydirectinput`, `keyboard`, and `time` installed via `pip install`.

If you are on a Windows 10+ machine, the easiest way to do this is to go to the Windows store and search for Python. Select any one of the versions 3.x (currently 3.7 - 3.10 are on there). Hit install.

After Python is installed, open the command prompt by going to search (hitting the Windows key), and typing in `cmd`. Then hit enter. After the prompt has opened, type in `pip install **module**`, where module is any one of the four `pyautogui`, `pydirectinput`, `keyboard`, and `time`.

Once all four are done, you will now need a IDE (integraded development environment). I highly recommend VSCode. Installing it is also easy. I recommend installing it from the [Microsoft website](https://code.visualstudio.com/download). Once it is installed, go to the extensions tab on the left side of the window, search for `python` and install the Python package made by Microsoft.

## Test Program To Detect Installation Issues

It is always recommended to test something simple out. So I will direct you to the always classic [Hello World Tutorial](https://code.visualstudio.com/docs/python/python-tutorial) specifically for VSCode.

If you encounter any issues such as it not running or saying it cannot detect Python, the link to the Hello World tutorial goes over proper installation from start to finish. 

## Setup

To use the program, open it with VSCode or paste it in. If you have downloaded the repository directly from GitHub, open the file `commandlist.txt`, otherwise, create it now. From here, you will need to find your commands list for whatever game. Paste the list into the text file. You will need to format it.

For each command to be ran, it needs to be on a line by itself. No other command or words can be on that line. Here is a functional example:

```
Medium Fossils
11 Apex
/spawnitem apexfossil1
/spawnitem apexfossil2
/spawnitem apexfossil3

12 Avian
/spawnitem avianfossil1
/spawnitem avianfossil2
/spawnitem avianfossil3
```

This will definitely work just fine. However, you can optimize it a little bit by removing things that are not commands. Here is the best input:

```
/spawnitem apexfossil1
/spawnitem apexfossil2
/spawnitem apexfossil3
/spawnitem avianfossil1
/spawnitem avianfossil2
/spawnitem avianfossil3
```

## Command Key vs Game Hotkey

Be aware of what game you are playing and the hotkeys that it has. Once started, the program waits on the command key to be pressed in order to start entering commands. This is to allow for any necessary setup. The default command key is `o`. If that is a hotkey in the game, you can either choose to disable that key in game (if possible), or change the command key for the program. The latter of which is probably the easiest depending on the game. Make sure to pick something that doesn't conflict with any other hotkeys in game.

## Running

To officially run the program, you can click the play button in the top right of the code window.

## Game Dependent Enter

Depending on the game, you may be entering commands into a dialogue box where you have to open it via `enter`. The same way you would talk in chat in some games. Examples include Starbound and World of Warcraft. Others use a full on console that require opening once and you just type in. Think Elder Scrolls and Fallout series.

If the game does use a console, a few lines will need to be commented out so they don't run. They wouldn't hurt anything, but it will take a decent amount longer. They are lines 50, 51, and 54. Seen below:

```
# If you have to open a dialogue to type, uncomment this
# Start with dialogue closed before running program
pydirectinput.press('enter')
print('first enter pressed')

# Delay by preCmdDelay seconds so the game can register
time.sleep(preCmdDelay)
```

To comment them out, simply add a `#` to the beginning. Like so:

```
# If you have to open a dialogue to type, uncomment this
# Start with dialogue closed before running program
# pydirectinput.press('enter')
# print('first enter pressed')

# Delay by preCmdDelay seconds so the game can register
# time.sleep(preCmdDelay)
```

## Issues

Should you encounter any issues, or something is not clear, feel free to submit an issue on GitHub!