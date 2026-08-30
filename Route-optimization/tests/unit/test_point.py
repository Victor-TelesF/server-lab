from domain.location import Point
import pytest
import numpy as np

def test_point_creation_valid():
    point = Point(3.0, 4.0)
    assert point is not None

def test_point_coordinate_returns_correct_array():
    point = Point(3.0, 4.0)
    expected = np.array([3.0, 4.0], dtype=np.float64)
    np.testing.assert_array_equal(point.coordinate, expected)

def test_point_rejects_nan_x():
    with pytest.raises(ValueError, match="X não pode ser NaN ou infinito"):
        Point(float('nan'), 4.0)

def test_point_rejects_nan_y():
    with pytest.raises(ValueError, match="Y não pode ser NaN ou infinito"):
        Point(3.0, float('nan'))

def test_point_rejects_infinite_x():
    with pytest.raises(ValueError, match="X não pode ser NaN ou infinito"):
        Point(float('inf'), 4.0)

def test_point_rejects_infinite_y():
    with pytest.raises(ValueError, match="Y não pode ser NaN ou infinito"):
        Point(3.0, float('inf'))

def test_point_rejects_negative_infinite_x():
    with pytest.raises(ValueError, match="X não pode ser NaN ou infinito"):
        Point(float('-inf'), 4.0)

def test_point_rejects_negative_infinite_y():
    with pytest.raises(ValueError, match="Y não pode ser NaN ou infinito"):
        Point(3.0, float('-inf'))