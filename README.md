# Screen Time CLI Log
### Video Demo:  

<URL HERE>

### Description:

The Screen Time CLI Log is a command line program coded entirely in Python 3.11, which enables the user to log and keep track of their screen time. The user can keep track of the screen time data of multiple profiles, which are visualized as a simple plot graph using Matplotlib. All data is tracked and stored using SQLite3. 

This program was designed as the final project for the HarvardX course [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/), instructed by David Malan. Particularly, this program was a way for me to better familiarize with the SQLite3 and Matplotlib libraries.

### Requirements and Installation:
Matplotlib is required for use of this program. It can be installed by running:

```shell
pip install matplotlib
```


A requirements.txt file is included with this program so that the user can alternatively install Matplotlib by running:

```shell
pip install -r requirements.txt
```

### Usage:

#### Windows:

```shell
python project.py
```

#### MacOS:

```shell
python3 project.py
```

Upon startup, a database is created if none already exists that stores names, dates and hours of screentime. The user is presented with several options in the CLI menu, and can type any of the given commands to proceed. The program will prompt the user to enter one of the listed commands if input does not correspond. 

```log``` - Type 'log' to log your name, the date, and the hours of screen time. The date must be in MM/DD format, and the hours of screen time logged must be an integer.

```graph``` - Type 'graph' to view a Matplotlib plot of a user's screen time. The program will prompt the user to select the name of the profile whose data the user would like to see visualized.

```delete``` - Type 'delete' to reset all data in the database. 

```credits``` - Type 'credits' to view program credits.

```exit``` - Type 'exit' to exit the program.

### Special Thanks:
* My wife Laura for being a constant source of inspiration and encouragement
* David Malan and the CS50 team at Harvard University for making CS50P accessible to the public

Created by Spencer Poulin 2023 \
[Github](www.github.com/sjpoulin)