class Block():
    def __init__(self):
        self.symbol = 'A'
        self.attributes = {
            'Solid':False
        }
    def showsymbol(self):
        return self.symbol
    def showattributes(self):
        return self.attributes
    def onCollision(self):
        pass
class Wall(Block):
    def __init__(self):
        self.symbol = 'W'
        self.attributes = {
            'Solid':True
        }
    def onCollision(self):
        pass
class Air(Block):
    def __init__(self):
        self.symbol = 'A'
        self.attributes = {
            'Solid':False
        }
    def onCollision(self):
        pass
class Transition(Block):
    def __init__(self, to):
        self.symbol = 'T'
        self.attributes = {
            'Solid':True
        }
        self.to = to
    def onCollision(self):
        global roomchange
        global roomto
        roomchange = True
        roomto = self.to
class Room():
    def __init__(self, structure, starting_pos):
        self.structure = structure
        self.pos = starting_pos
    def move(self, direction):
        global newpos
        newpos = self.pos
        gaveerror = False
        match direction:
            case 'w':
                lookat = [self.pos[0], self.pos[1] - 1]
            case 's':
                lookat = [self.pos[0], self.pos[1] + 1]
            case 'a':
                lookat = [self.pos[0] - 1, self.pos[1]]
            case 'd':
                lookat = [self.pos[0] + 1, self.pos[1]]
        try:
            lookobject = self.structure[lookat[1]][lookat[0]]
            objectattributes = lookobject.showattributes()
            if(objectattributes['Solid'] == False):
                newpos = lookat
            lookobject.onCollision()
        except IndexError:
            gaveerror = True
        if(newpos[0] > -1 and newpos[1] > -1 and gaveerror == False):
            self.pos = newpos
    def showroom(self):
        currentY = 0
        for row in self.structure:
            rowfull = []
            currentX = 0
            for block in row:
                blocksymbol = block.showsymbol()
                if(currentX == self.pos[0] and currentY == self.pos[1]):
                    rowfull.append('P')
                else:
                    rowfull.append(blocksymbol)
                currentX += 1
            print(rowfull)
            currentY += 1
    def playerpos(self):
        return self.pos
class Map():
    def __init__(self, rooms):
        self.rooms = rooms
        self.current_room = self.rooms[0]
    def showroom(self):
        self.current_room.showroom()
    def move(self, direction):
        global roomchange
        roomchange = False
        self.current_room.move(direction)
        if(roomchange == True):
            global roomto
            self.current_room = self.rooms[roomto]
    def details(self):
        return [self.current_room.playerpos(), self.current_room]