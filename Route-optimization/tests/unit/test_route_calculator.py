from domain.route_calculator import RouteCalculator
from domain.location import Point
import pytest


def test_distance_between_known_values():
    a = Point(0.0, 0.0)
    b = Point(3.0, 4.0)
    distance = RouteCalculator.distance_between(a, b)
    assert distance == 5.0

def test_distance_between_is_symmetric():
    a = Point(1.0, 2.0)
    b = Point(4.0, 6.0)
    distance_ab = RouteCalculator.distance_between(a, b)
    distance_ba = RouteCalculator.distance_between(b, a)
    assert distance_ab == distance_ba

def test_distance_between_same_point_is_zero():
    a = Point(3.0, 4.0)
    distance = RouteCalculator.distance_between(a, a)
    assert distance == 0.0

def test_total_distance_empty_list():
    calculator = RouteCalculator([])
    distance = calculator.total_distance()
    assert distance == 0.0

def test_total_distance_single_point():
    calculator = RouteCalculator([Point(3.0, 4.0)])
    distance = calculator.total_distance()
    assert distance == 0.0

def test_total_distance_multiple_points():
    points = [Point(0.0, 0.0), Point(3.0, 4.0), Point(6.0, 8.0)]
    calculator = RouteCalculator(points)
    distance = calculator.total_distance()
    assert distance == 10.0

def test_total_distance_order_matters():
    points1 = [Point(0.0, 0.0), Point(3.0, 4.0), Point(6.0, 0.0)]
    points2 = [Point(0.0, 0.0), Point(6.0, 0.0), Point(3.0, 4.0)]
    calculator1 = RouteCalculator(points1)
    calculator2 = RouteCalculator(points2)
    distance1 = calculator1.total_distance()
    distance2 = calculator2.total_distance()
    assert distance1 != distance2

def test_nearest_neighbor_empty_list_raises_error():
    calculator = RouteCalculator([])
    with pytest.raises(ValueError, match="Lista não pode estar vazia"):
        calculator.nearest_neighbor()

def test_nearest_neighbor_single_point():
    point = Point(3.0, 4.0)
    calculator = RouteCalculator([point])
    route = calculator.nearest_neighbor()
    assert len(route) == 1
    assert route[0] == point

def test_nearest_neighbor_visits_all_points_once():
    points = [Point(0.0, 0.0), Point(3.0, 4.0), Point(6.0, 8.0)]
    calculator = RouteCalculator(points)
    route = calculator.nearest_neighbor()
    assert len(route) == 3
    assert len(set(route)) == 3

def test_nearest_neighbor_does_not_mutate_original_list():
    points = [Point(0.0, 0.0), Point(3.0, 4.0), Point(6.0, 8.0)]
    original_points = points.copy()
    calculator = RouteCalculator(points)
    calculator.nearest_neighbor()
    assert points == original_points