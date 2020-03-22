import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError, FailRobotError


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        asteroid = Asteroid(x, y)
        direction = "N"
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "W")


class TestTurns:

    def setup(self):
        self.x, self.y = 10, 15
        self.asteroid = Asteroid(self.x, self.y)

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
                ("E", "N"),
        )
    )
    def test_turn_left(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("N", "E"),
                ("E", "S"),
                ("S", "W"),
                ("W", "N"),
        )
    )
    def test_turn_right(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_right()
        assert robot.direction == expected_direction


class TestMoves:

    def setup(self):
        self.x, self.y = 5, 10
        self.asteroid = Asteroid(self.x, self.y)

    @pytest.mark.parametrize(
        "current_position,expected_position",
        (
                ((5, 10), (6, 10)),
                ((5, 10), (5, 11)),
        )
    )
    def test_move_forward(self, current_position, expected_position):
        robot = Robot(self.x, self.y, self.asteroid, current_position)
        robot.move_forward()
        assert robot.x, robot.y == expected_position

    @pytest.mark.parametrize(
        "current_position,expected_position",
        (
                ((5, 10), (4, 10)),
                ((5, 10), (5, 9)),
        )
    )
    def test_move_backward(self, current_position, expected_position):
        robot = Robot(self.x, self.y, self.asteroid, current_position)
        robot.move_backward()
        assert robot.x, robot.y == expected_position

    @pytest.mark.parametrize(
        "asteroid_size,current_position,expected_position",
        (
                ((5, 10), (5, 10), (6, 10)),
                ((5, 10), (5, 10), (5, 11)),
        )
    )
    def test_check_if_robot_falls_from_asteroid(self, asteroid_size, current_position, expected_position):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*expected_position, asteroid, "W")
