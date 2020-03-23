# tcod-start-examples

##### Little examples to start with tcod for your own game

Preamble:

Hi Folks,

https://rogueliketutorials.com/ inspires this project, and there were only two things that led to this version.
First, I struggled with the deprecated signs shown in PyCharm and I wanted to get rid of them.
Second, I started the 100-day challenge to learn python. The last 20 years, I have mainly coded in PHP and java. Before that, I have had a look (or two) in C++, C#, C, LPC, Amos (Amiga), C64 assembler and Basic, VBasic6 and some more I already have forgotten (oh yes, JavaScript of course). With that many languages, I have found some things - some guidelines and best practice, that I actively like - and some, that not. One (in my humble opinion) lousy habit within the python-community seems to be: long codes, many indents and sort of rapid code. Nothing wrong with that, but I often struggle with that and yes, I started to learn python to 'look beyond tellerrand' (german for 'edge of a plate') and find new methods that I might use in PHP but in return, I'll use the other way as well ;)
Third, (did I say just two?) the roguelike tutorials were brilliant, but in the end, I tried to refactor it for nearly 4 days and there where more and more 'what the heck' moments. So I decided to start over, and from scratch - and with that experience, I would like to share this all with you.

So - you might not like everything I make. Please start to compare this project with roguelike tutorials and decide which approach you like more. Maybe you'll find your mixture for your own game, and you also can give something in return - but please be gentle. At least, remember where you would be standing, without any tutorials and examples.

Tl/Dr: This is a few from a PHP coder into the python and roguelike community. Feel free to use this code for your own purpose, and if you like, contribute to this project or leave comments on twitter @dulldaydudes

#### Install and start (PyCharm on mac)

- Clone project from git@github.com:dulldaydudes/tcod-start-examples.git
- Add tcod
  - Open PyCharm>Preferences>Project >> Project Interpreter
  - click on [+]
  - search 'tcod'
  - click 'install'
- Setting up execute file
  - click on the python symbol and 'v' dropdown on the right side of the menu beside the play button
  - [Edit Configuration]
  - [+] (top left corner)
  - Select 'Python'
  - Select 'Script Path'
  - Have a look for 'app.py' file
  - Apply/Ok
  
Have fun

##### Why I did things, the way I did

As you might have read within the preamble, I did some things differently, then you might find in other python projects. Here some reasons why I think, this way has some benefits. When you can follow my argumentation - start to adopt this. If not, change it the way, you like it ;)

First of all, I try to use DDD and Solid. Within a new language, it's not always that simple, and there will be some parts where I can't achieve that goal - sorry for that. 

Because of that, you will find more folders and much more files. You also will see that I nearly always will use strong type binding. In the third place, my classes and devs will only use a few params. If there is a need to use more, I try to use factories to simplify things.

To be continued...
