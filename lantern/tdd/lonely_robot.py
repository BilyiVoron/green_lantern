class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        self.position = x, y
        if self.x > self.asteroid.x or self.y > self.asteroid.y:
            raise MissAsteroidError()

    def turn_left(self):
        left_turns = {"E": "N", "N": "W", "W": "S", "S": "E"}
        self.direction = left_turns.get(self.direction, None)

    def turn_right(self):
        right_turns = {"E": "S", "S": "W", "W": "N", "N": "E"}
        self.direction = right_turns.get(self.direction, "E")

    def move_forward(self):
        forward_moves = {self.position: self.x + 1 or self.y + 1}
        self.position = forward_moves.get(self.position, None)

    def move_backward(self):
        backward_moves = {self.position: self.x - 1 or self.y - 1}
        self.position = backward_moves.get(self.position, None)


class MissAsteroidError(Exception):
    pass


class FailRobotError(Exception):
    pass
