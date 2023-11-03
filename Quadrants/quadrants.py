
class Quadrant:
    patterns = []
    quadrant_number = -1

    @classmethod
    def checkPattern(cls, neighbor_pattern):
        for pattern in cls.patterns:
            if neighbor_pattern == pattern:
                return cls.quadrant_number
        return None

class Quadrant0(Quadrant):
    patterns = [0, 0, 0, 0]
    quadrant_number = 0

class Quadrant1(Quadrant):
    #patterns = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    patterns = [[255, 0, 0, 0], [0, 255, 0, 0], [0, 0, 0, 255], [0, 0, 255, 0]]
    quadrant_number = 1

class Quadrant2(Quadrant):
    #patterns = [[1, 1, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1], [1, 0, 1, 0]]
    patterns = [[255, 255, 0, 0], [0, 255, 0, 255], [0, 0, 255, 255], [255, 0, 255, 0]]
    quadrant_number = 2

class Quadrant3(Quadrant):
    #patterns = [[1, 1, 0, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 0]]
    patterns = [[255, 255, 0, 255], [0, 255, 255, 255], [255, 0, 255, 255], [255, 255, 255, 0]]
    quadrant_number = 3

class Quadrant4(Quadrant):
    #patterns = [[1, 1, 1, 1]]
    patterns = [[255, 255, 255, 255]]
    quadrant_number = 4


class QuadrantD(Quadrant):
    #patterns = [[1, 0, 0, 1], [0, 1, 1, 0]]
    patterns = [[255, 0, 0, 255], [0, 255, 255, 0]]
    quadrant_number = 5


def matchPattern(neighbor_pattern):
    # Check all of the Quadrant patterns, check which one matches
    if Quadrant0.checkPattern(neighbor_pattern):
        return 0
    elif Quadrant1.checkPattern(neighbor_pattern):
        return 1
    elif Quadrant2.checkPattern(neighbor_pattern):
        return 2
    elif Quadrant3.checkPattern(neighbor_pattern):
        return 3
    elif Quadrant4.checkPattern(neighbor_pattern):
        return 4
    else:
        return 5


print(matchPattern([1, 1, 1, 1]))




