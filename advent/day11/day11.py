

class Cube:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "[Cube: {},{},{} ]".format(self.x, self.y, self.z)


def distance(a, b):
        return max(abs(a.x - b.x), abs(a.y - b.y), abs(a.z - b.z))


def fn(txt):
    directions = txt.split(",")
    
    furthest = 0
    position = Cube()

    cube_directions = {
        "nw":Cube(+1, -1,  0),
        "n":Cube(+1,  0, -1),
        "ne":Cube(0, +1, -1),
        "se":Cube(-1, +1,  0),
        "s":Cube(-1,  0, +1),
        "sw":Cube(0, -1, +1)
    }

    for step in directions:
        direction = cube_directions[step]

        position.x += direction.x
        position.y += direction.y
        position.z += direction.z

        pos_distance = distance(position, Cube())
        if pos_distance > furthest:
            furthest = pos_distance

    return distance(position, Cube()), furthest
