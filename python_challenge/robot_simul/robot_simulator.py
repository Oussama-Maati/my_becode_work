NORTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot():
    def __init__(self, face, x, y):
        self.bearing = face
        self.coordinates = (x, y)


    # def turn_right(self):
    #     match self.bearing:
    #         case SOUTH: