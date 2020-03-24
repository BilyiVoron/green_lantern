class Asteroid:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Obstacle:
    def __init__(self, x_obstacle, y_obstacle, asteroid):
        self.x = x_obstacle
        self.y = y_obstacle
        self.asteroid = asteroid


class Robot:
    def __init__(self, x, y, asteroid, direction, obstacle):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        self.obstacle = obstacle
        self.position = x, y
        if not (self.asteroid.a >= self.x >= 0 and self.asteroid.b >= self.y >= 0):
            raise MissAsteroidError
        elif self.x == self.obstacle.x or self.y == self.obstacle.y:
            raise ObstacleRobotError

    def turn_left(self):
        left_turns = {"E": "N", "N": "W", "W": "S", "S": "E"}
        self.direction = left_turns.get(self.direction, "N")

    def turn_right(self):
        right_turns = {"E": "S", "S": "W", "W": "N", "N": "E"}
        self.direction = right_turns.get(self.direction, "N")

    def move_forward(self):
        forward_moves = {self.position: self.x + 1 or self.y + 1}
        self.position = forward_moves.get(self.position, None)

    def move_backward(self):
        backward_moves = {self.position: self.x - 1 or self.y - 1}
        self.position = backward_moves.get(self.position, None)


class MissAsteroidError(Exception):
    def __str__(self):
        return "Oops! Your robot missed from asteroid!"


class ObstacleRobotError(Exception):
    def __str__(self):
        return "Oops! Your robot has some obstacle on his way!"
