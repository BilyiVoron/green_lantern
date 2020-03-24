import pytest
from lonely_robot import (
    Robot,
    Asteroid,
    Obstacle,
    MissAsteroidError,
    ObstacleRobotError,
)


class TestRobotCreation:
    def test_parameters(self):
        a, b = 20, 20
        asteroid = Asteroid(a, b)
        x_obstacle, y_obstacle = 7, 11
        obstacle = Obstacle(x_obstacle, y_obstacle, asteroid)
        x, y = 10, 15
        direction = "N"
        robot = Robot(x, y, asteroid, direction, obstacle)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid
        assert robot.obstacle == obstacle

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates,obstacle_position",
        (
                ((15, 25), (26, 30), (12, 17)),
                ((15, 25), (26, 24), (12, 17)),
                ((15, 25), (15, 27), (12, 17)),
                ((15, 25), (-2, 27), (12, 17)),
                ((15, 25), (15, -3), (12, 17)),
                ((15, 25), (-2, -3), (12, 17)),
        ),
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates, obstacle_position):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            obstacle = Obstacle(*obstacle_position, asteroid)
            Robot(*robot_coordinates, asteroid, "W", obstacle)


class TestTurns:
    def setup(self):
        self.a, self.b = 10, 15
        self.asteroid = Asteroid(self.a, self.b)
        self.x_obstacle, self.y_obstacle = 7, 11
        self.obstacle = Obstacle(self.x_obstacle, self.y_obstacle, self.asteroid)
        self.x, self.y = 10, 15

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
                ("E", "N"),
        ),
    )
    def test_turn_left(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction, self.obstacle)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("N", "E"),
                ("E", "S"),
                ("S", "W"),
                ("W", "N"),
        ),
    )
    def test_turn_right(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction, self.obstacle)
        robot.turn_right()
        assert robot.direction == expected_direction


class TestMoves:
    @pytest.mark.parametrize(
        "direction,current_position,expected_position",
        (
                ("N", (5, 10), (5, 11)),
                ("E", (5, 10), (6, 10)),
                ("S", (5, 10), (5, 9)),
                ("W", (5, 10), (4, 10)),
        )
    )
    def test_move_forward(self, current_position, expected_position, direction):
        robot = Robot(self.x, self.y, self.asteroid, current_position, self.obstacle)
        robot.move_forward()
        assert robot.x, robot.y == expected_position

    def setup(self):
        self.a, self.b = 10, 15
        self.asteroid = Asteroid(self.a, self.b)
        self.x_obstacle, self.y_obstacle = 7, 11
        self.obstacle = Obstacle(self.x_obstacle, self.y_obstacle, self.asteroid)
        self.x, self.y = 10, 15

    @pytest.mark.parametrize(
        "direction,current_position,expected_position",
        (
                ("N", (5, 10), (5, 9)),
                ("E", (5, 10), (4, 10)),
                ("S", (5, 10), (5, 11)),
                ("W", (5, 10), (6, 10)),
        )
    )
    def test_move_backward(self, current_position, expected_position, direction):
        robot = Robot(self.x, self.y, self.asteroid, current_position, self.obstacle)
        robot.move_backward()
        assert robot.x, robot.y == expected_position

    @pytest.mark.parametrize(
        "current_position,expected_position,obstacle_position",
        (
                ((5, 10), (6, 10), (6, 10)),
                ((5, 10), (5, 11), (5, 11))
        ),
    )
    def check_if_robot_have_no_obstacles(self, expected_position, obstacle_position):
        with pytest.raises(ObstacleRobotError):
            obstacle = Obstacle(*obstacle_position)
            Robot(*expected_position, obstacle, "W")
