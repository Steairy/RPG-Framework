# RPG-Framework
Framework to make basic RPG games in python

# How to use
Download framework.py and put it in the same folder as your other project and import it by writing

```
import framework
```
To start using the framework, you have to make rooms first

Here is an example of a room:
```
myRoom = framework.Room([[framework.Wall(), framework.Air()], [framework.Air(), framework.Air()]], [1, 0])
```
The first parameter in the room is an array, and every single array in that array is a row.

In the example, the first row was a Wall and an Air. These blocks come with the framework.


The second parameter is the starting position in the level. It has to be an array. The first position is the x value, the second one is the y. 0, 0 is the top left of the screen.

After you made your rooms, you can put them in a map like this:
```
map = framework.Map([room1, room2])
```
**Enter your rooms as an array. The order of the rooms is also important**
# Functions of a map

### showroom
This shows the room you are currently in using block symbols
### move(direction)
This function allows you to move in one of the 4 directions.

This function can only take in the inputs of wasd on lowercase
### details
Gives you the coordinates of the player and the current room
# Blocks
Every room consists of blocks, the framework comes with 3 blocks
### Wall
You can't move into this
### Air
Default tile
### Transition(number)
Allows you to change the room you are in

The number is the element of the room list the room is gonna change to. For Example:
```
map = framework.Map([room1, room2])
```
If this was the room and we used Transition(0), after going through the transition we would end up in room1
## How to make your own blocks
Make a class that's inherited from the class 'Block'
```
class NewBlock(Block):
```
on init, enter a symbol for this new block on the 'self.symbol' variable. make a list called self.attributes and put if you want this block to be solid or not. If solid is false, you will be able to move on top of it. You can also put any specific variables you need for this block here
```
def __init__(self):
  self.symbol = 'A'
  self.attributes = {
    'Solid':False
}
```
Make a function called 'onCollision'. Do not put any perimeters into this. This function is what will happen when the player moves to this block. I used pass here but you can put anything you want
```
def onCollision(self):
        pass
```

## Extra Info
There is a global variable called 'newpos', if you change this on the onCollision function, you can change the Player's position. There are 2 other global variables called roomchange and roomto.

If you set roomchange to True, you can set a number for roomto and change rooms like that. The number affects the room same way the number in Transition does. 
