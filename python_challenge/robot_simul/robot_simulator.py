NORTH = "NORTH"
EAST = "EAST"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot():
    def __init__(self, face=NORTH, x=0, y=0):
        self.bearing = face
        self.coordinates = (x, y)

    def simulate(self, way):
        for letter in way:
            if letter == "A":
                self.advance()
            elif letter == "R":
                self.turn_right()
            elif letter == "L":
                self.turn_left()


    def turn_right(self):
        match self.bearing:
            case "SOUTH":
                self.bearing = "WEST"
            case "NORTH":
                self.bearing = "EAST"
            case "EAST":
                self.bearing = "SOUTH"
            case "WEST":
                self.bearing = "NORTH"

    def turn_left(self):
        match self.bearing:
            case "SOUTH":
                self.bearing = "EAST"
            case "NORTH":
                self.bearing = "WEST"
            case "EAST":
                self.bearing = "NORTH"
            case "WEST":
                self.bearing = "SOUTH"

    def advance(self):
        match self.bearing:
            case "SOUTH":
                self.coordinates = (self.coordinates[0], self.coordinates[1]-1)
            case "NORTH":
                self.coordinates = (self.coordinates[0], self.coordinates[1]+1)
            case "EAST":
                self.coordinates = (self.coordinates[0]+1, self.coordinates[1])
            case "WEST":
                self.coordinates = (self.coordinates[0]-1, self.coordinates[1])