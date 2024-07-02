
# PyGame Tutorial

## Origin Acknowledgement
This project was created by me, BStew794, but I am coding this based off a tutorial from the Youtuber "Clear Code" from 2 years ago (https://www.youtube.com/watch?v=AY9MnQ4x3zk&list=WL&index=2).

## Summary and Purpose
The purpose of this project is to teach me some of the basics of the PyGame package/library for Python after I attempted to jump in on my own unique project and got off track trying to do everything manually myself including a frustrating collision system. The game is fully playable with music, jump sounds, and animations currently. Unforunately, the graphics and sounds are not my own but from Clear Code's repo. Considering that it is simple pixel art, I may try my own hand at drawing some replacements since I now know the dimesions. Some of the logic is more custom to my particular taste and style. I plan to continue to add more of my own special logic, and I would like to practice training some machine learning agents to play the game eventually. For this reason, A license is included for your convience, in case you want to clone the repository and do some of your own work on it.

As of right now, I plan to let this project sit while I go learn more about PyGame Masks for near pixel perfect collision before returning to the Python version of my spaceship combat game.

## Installation Instructions
### Install Python
This project was coded in Python 3.12.2 but later versions should work. You will need to go to https://www.python.org/downloads/ and click the yellow button that says 'Download Python x.xx.x'. x.xx.x will be the most recent version release. At the time of writing this, it reads 3.12.4.

You will need to install Python after downloading it from Python.org. You can do so by going to your downloads folder and double clicking the python.exe file that was downloaded. Where this is found depends on your Operating System. The name of the file may also change depending on the version dowloaded, and your CPU brand and architecture.

Follow the instructions for a default set-up unless you'd like to customize it. I make no promises that the program will run probably if you do that though.

### Install PyGame 
There are multiple ways to install the PyGame Python package, but we will use the pip installer here. When downloading and installing Python from python.org, pip is automatically installed.

Firstly, you will need to open your OS console. The rest of these instructions are geared more towards a Windows OS user. If you are on a windows system, you can type 'cmd' into the search bar and click on 'Command Prompt' to open a console window. It should currently point to your user folder on the drive that the OS was installed on.

This is a great time to double check that Python was installed properly. You can do this by typing 'python -v' ('python -version' on a linux system) and then pressing Enter on your keyboard. Every command I tell you to type in these instructions need to have Enter pressed afterwards. A bunch of text should appear in the console window and at the bottom you should see a line starting with 'Python' followed by the current version number that is installed. The console will post something similar to "'Python' is not recognized as an internal or external command,
operable program or batch file." if Python was not installed properly. If so, you may need to make sure that Python was added to your PATH variable correctly which is something I do not feel confident enough to explain here.

After verifying the installation of Python, we can now install the PyGame package by typing the command, 'pip install pygame'. The console will print an error message similar to 'ERROR: Could not find a version that satisfies pygame' if the process did not work. The best advice I have is to make sure that pip is up to date witht eh altest version. You can update pip with the command, 'python.exe -m pip install --upgrade pip' or 'pip install --upgrade pip', dependening on your OS. If pygame still refuses to install then I'd recommend seeking further help from anotehr professional.

### Install Git
I hope you've kept that console terminal open, because we have more work to do. How you install Git will vary wildly depending on your OS. I will detail the Linux and Windows approaches here.

#### Windows OS
Go to gitforwindows.org and click the blue 'Download' button.

Go to your downloads folder and double click on the git.exe file. The name may vary slightly based on on the version dowloaded, and your CPU brand and architecture.

I recommend reading through the GNU Public license that pops up that will detail things regarding to your rights and priledges with regards to the Git software . Once you are done, click 'Install'.

The installation may take a few seconds. After it is done, a new window will pop up affirming that Git is now installed on your computer. Now, you can click the 'Finish' button. You can have Git Bash launch and read release notes directly after clicking 'Finish', but I leave that to your discretion.

You can verify that git is installed by typing the command 'git -v' into your console terminal which will display the current version. If it returns an error, then you may need to repeat the installation steps or perform some reasearch of your own to fix it.

#### Linux OS
Installing Git on Linux is easier since it was originally developed to serve as a version control system for Linux. You can natively use your package management tool to install git. For Ubuntu it is 'apt'. You will need to open your console terminal.

it is generally a good idea to make sure that apt is up to date with the latest version. You can update apt with teh following command, 'sudo apt-get update'

Now, you can install Git with the following command, 'sudo apt-get install git-all'.

You can verify the installation with the console command 'git version'. If it returns an error, then you may need to repeat the installation steps or perform some reasearch of your own to fix it.

### Clone the Repository Locally
Hopefully you've kept your console terminal open. Otherwise, get a console window open.

Navigate to where you want to place my repository. Usually you can do so by typing 'cd' followed by the name of sub-directory you want to go to; don't forget to add spaces between the 'cd' command and the sub-directory name. If you're unsure of what directories you can currently travel to then you can type 'dir' to have a list of current sub-directories printed to the console window. Ypu can also use 'cd ..' to go up a directory. If you do not have a folder already created to hold the repository then you will need to make one. There are many ways to do this, but you can type 'mkdir' followed by the name you want to give the new directory/folder. Then use the 'cd' command to navigate to it.

Next, use the command, 'git clone https://github.com/bstew794/PyGame_Tutorial' to download a clone of the repository inside of the folder that you invoked the command in. You now have everything you need to play the game!

## Play Instructions
Make sure to finish the installation instructions section before attempting to follow the steps of this section.

Firstly, navigate to where you cloned the GitHub project Repository. Make sure that your current directory contains 'Runner.py'.

Run the following command 'python runner.py'

The game will now open and you can press the spacebar on your keyboard to begin playing. The spacebar also causes the player character to jump over obstacles. You can also click on the player character itself to make it jump, but it may be slightly more diffcult to clear obstacles that way.

Enjoy!
