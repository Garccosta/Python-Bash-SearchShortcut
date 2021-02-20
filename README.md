# Python Bash Search Shortcut

This project uses some python and bash scripts to quickly search
the web using shortcuts in the Terminal(Shell/prompt). 

It was inspired by "Automating the Boring Stuff with Python Programming" book/course.

## How it works

You type in the Terminal or on Windows Run command dialog box(shortcut: "Windows key + R") the bat file name along with the arguments to be searched with blank spaces separating them. 

Example:

```
mapit New York
```

This will run the "mapit" bat script, which in turn will run the python script with the same name. 
In this example, this command will open a new web browser tab and search for "New York" in Google Maps.

If you don´t pass any arguments the script will search for what is recorded in your clipboard.

There are currently 5 quick search shortcuts:

```
mapit: Will search on Google Maps;
bookit: Will search on Booking.com;
googleit: Will search on Google.com;
shopit: Will search on Aliexpress, Amazon and Americanas.com;
youtubeit: Will search on Youtube;
```

## How to Get Started

### 1. Fist clone the repo to some directory of your choice. 

Copy its location, you will use it later on ;)


### 2. You will need Python in order to run the '.py' scripts. 

You can download it in its official website: https://www.python.org/downloads/



### 3. Download the third party python package: pyperclip.

If you open the cloned project with an IDE with the proper Python Extension installed,
it will probably automatically find the missing package and prompt you to download it. 



### 4. Change the directory path in the .bat files

Change the "LOCATION_HERE" string in the .bat code files for the directory you cloned the project.


### 5. Finally add the path to the System Environment Variables 

Add the directory path where you cloned the project in the "Edit the system environment variables" Control Panel.

In Windows you can easily find it by searching "environment". 

In "Environment Variables..." add it to the Path registry under User or System Variables.

### Done! 

Now you can quickly search the web by using one of the scripts on the folder and customize it anyway you want!

You can change the scripts names and create new ones for your search specific needs! ;)

