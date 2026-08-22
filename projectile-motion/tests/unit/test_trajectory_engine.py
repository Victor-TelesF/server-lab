import pytest
from domain.launch_config import LaunchConfig
from domain.trajectory_engine import TrajectoryEngine


@pytest.fixture
def engine_45_degrees():
    config = LaunchConfig(v0=20, angle_deg=45, gravity=9.81)
    return TrajectoryEngine(config)

def test_position_at_zero_is_origin(engine_45_degrees):
    assert engine_45_degrees.position_at(0) == pytest.approx((0, 0), abs=1e-9)


def test_values_match_manual_calculation_at_45_degrees(engine_45_degrees):

    v0 = 20
    g = 9.81
    t = 1
    expected_x = v0 * (2 ** 0.5 / 2) * t  
    expected_y = v0 * (2 ** 0.5 / 2) * t - 0.5 * g * t**2
    x, y = engine_45_degrees.position_at(t)
    assert x == pytest.approx(expected_x, rel=1e-2)
    assert y == pytest.approx(expected_y, rel=1e-2)

def test_max_height_is_positive(engine_45_degrees):
    _, max_height = engine_45_degrees.max_height()
    assert max_height > 0

def test_trajectory_has_no_negative_y(engine_45_degrees):
    t_flight = engine_45_degrees.time_of_flight()
    times = [t_flight * i / 100 for i in range(101)]

    for t in times:
        _, y = engine_45_degrees.position_at(t)
        assert y >= -1e-9 

def test_trajectory_ends_near_zero(engine_45_degrees):
    t_flight = engine_45_degrees.time_of_flight()
    _, y = engine_45_degrees.position_at(t_flight)
    assert y == pytest.approx(0, abs=0.01)

def test_negative_time_raises_error(engine_45_degrees):
    with pytest.raises(ValueError):
        engine_45_degrees.position_at(-1)

def test_angle_zero_is_allowed():
    config = LaunchConfig(v0=20, angle_deg=0, gravity=9.81)
    engine = TrajectoryEngine(config)
    t_peak, height = engine.max_height()
    assert t_peak == pytest.approx(0, abs=1e-9)
    assert height == pytest.approx(0, abs=1e-9)

def test_trajectory_points_returns_correct_number_of_points(engine_45_degrees):
    num_points = 10
    points = engine_45_degrees.trajectory_points(num_points)
    assert len(points) == num_points + 1

def test_trajectory_points_with_invalid_num_points_raises_error(engine_45_degrees):
    with pytest.raises(ValueError):
        engine_45_degrees.trajectory_points(0)

def test_trajectory_points_with_negative_num_points_raises_error(engine_45_degrees):
    with pytest.raises(ValueError):
        engine_45_degrees.trajectory_points(-5)

def test_trajectory_points_first_point_is_origin(engine_45_degrees):
    points = engine_45_degrees.trajectory_points(10)
    first = points[0]
    assert first["t"] == pytest.approx(0, abs=1e-9)
    assert first["x"] == pytest.approx(0, abs=1e-9)
    assert first["y"] == pytest.approx(0, abs=1e-9)

def test_trajectory_points_last_point_ends_near_zero(engine_45_degrees):
    points = engine_45_degrees.trajectory_points(10)
    last = points[-1]
    assert last["y"] == pytest.approx(0, abs=0.01)