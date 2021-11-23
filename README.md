# Kodelock
a tool to assist in code raiding in rust

This tool is designed to be used on a second monitor.

This tools will allow you to see a easily readable code to put in when code raiding and it allows you to go forwards and backwards without left and right arrows so you don't have to quench your eyes to see the code you were at in that .txt file and you don't even need to tab out!
It has a feature to "start from" whichever line you wish to, so if there is multiple people using this tool at once it is possible to coordinate who will be using codes from what line eg. 1st person from 0-300 2nd from 300-600 and so on.

To launch this tool you will need python3 and you will need to install 2 libraries for it.

How to install:   (If you have erros go all the way to the bottom to find a solution)

1) Download python3 and install it: https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
2) Continue the install on default settings unless you personally wish to change something.
3) When installed search python in your search bar and open a python command promp to check if it's install properly.
4) After that search up cmd and open it. In it you will write: pip install pillow pynput 
5) When you're done installing(It should only take about 5sec) open the Kodelock.py or Launch.bat file to launch

Alternativley you could open command prompt cd into the directory of Kodelock and launch it directly with  python Kodelock.py

In case something isn't working for you and you've followed the instructions message me on discord ITzViks#7482
![preview](https://user-images.githubusercontent.com/66530955/142982262-1332ceb8-1110-4fb6-8f17-d4e8bd5ec5fa.png)

I'm pretty sure rust doesn't even work on linux but if you're using linux you need to install the following:

sudo apt-get install python3-pil.imagetk

sudo apt-get install python3-tk

sudo apt-get install python3-pip

pip install pynput

.

.

.

.

.

If you're having issuses with pip dropping erros like not found externally or internally or something along those lines do the following:

1) Search cmd and open it
2) Type: setx PATH %PATH%;C:\Python310/Scripts and press enter

If you don't get a confirmation message "Save draft" (something along those lines)
Change the path like this:

1) Open cmd and type setx PATH %PATH%;
2) Search python and right click python 3.10 or whichever version you have installed and open file location
3) Once opened it should llead you to a folder with 4 files right click "Python3.10 (64-bit) open file location again 
4) Now open the Scripts folder and copy the path. (This is a path) ![scripts](https://user-images.githubusercontent.com/66530955/143000977-0e7635ad-60d2-41e2-9c56-84993c79b7f1.png)
NOTE: I have python 3.9 installed yours should be 3.10 but as long as it's a 3.X it'll work
6) Once copied put that on setx PATH %PATH%;C: so it should look like this
setx PATH %PATH%;C:<Path you copied> 
7) Press Enter (You might have to give it a minute after the draft completes) 
