class Asteroid:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Obstacle:
    def __init__(self, x_obstacle, y_obstacle, asteroid):
        self.x = x_obstacle
        self.y = y_obstacle
        self.asteroid = asteroid
        if any([self.asteroid.a < self.x, self.x < 0, self.asteroid.b < self.y, self.y < 0]):
            raise ObstaclePositionError


class Robot:
    def __init__(self, x, y, asteroid, direction, obstacle):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        self.obstacle = obstacle
        self.position = x, y
        if any([self.asteroid.a < self.x, self.x < 0, self.asteroid.b < self.y, self.y < 0]):
            raise OutsideAsteroidError
        elif any([self.x == self.obstacle.x, self.y == self.obstacle.y]):
            raise ObstacleRobotError

    def turn_left(self):
        left_turns = {"E": "N", "N": "W", "W": "S", "S": "E"}
        self.direction = left_turns.get(self.direction, "N")
        # if left_turns == {"E": "W", "N": "S", "W": "E", "S": "N"}:
        #     raise DirectionRobotError

    def turn_right(self):
        right_turns = {"E": "S", "S": "W", "W": "N", "N": "E"}
        self.direction = right_turns.get(self.direction, "N")
        # if right_turns == {"E": "W", "N": "S", "W": "E", "S": "N"}:
        #     raise DirectionRobotError

    def move_forward(self):
        forward_moves = {
            "N": {self.position: (self.x, self.y + 1)},
            "E": {self.position: (self.x + 1, self.y)},
            "S": {self.position: (self.x, self.y - 1)},
            "W": {self.position: (self.x - 1, self.y)},
        }
        self.position = forward_moves.get(self.direction)

    def move_backward(self):
        backward_moves = {
            "N": {self.position: (self.x, self.y - 1)},
            "E": {self.position: (self.x - 1, self.y)},
            "S": {self.position: (self.x, self.y + 1)},
            "W": {self.position: (self.x + 1, self.y)},
        }
        self.position = backward_moves.get(self.direction)


class OutsideAsteroidError(Exception):
    def __str__(self):
        return "Oops! Your robot can't be outside of the asteroid!"


class ObstaclePositionError(Exception):
    def __str__(self):
        return "Error! Obstacles can't be outside of the asteroid!"


class ObstacleRobotError(Exception):
    def __str__(self):
        return "Oops! Your robot has some obstacle on his way!"


# class DirectionRobotError(Exception):
#     pass
