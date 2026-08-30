from .location import Point
import numpy as np

class RouteCalculator:
    """Calculates distances and optimizes routes between points.

    This class encapsulates behavior and calculations over a collection
    of Point objects, including total distance calculation and nearest
    neighbor algorithm for route optimization.
    """

    def __init__(self, points: list[Point]):
        """Initializes a RouteCalculator with a list of points.

        Args:
            points (list[Point]): List of Point objects that compose the route.
        """
        self._points = points.copy()

    @property
    def points(self) -> list[Point]:
        """Returns a copy of the route's point list.

        Returns:
            list[Point]: Copy of the point list stored in RouteCalculator.
        """
        return self._points.copy()

    @staticmethod
    def distance_between(a: Point, b: Point) -> float:
        """Calculates the Euclidean distance between two points.

        Args:
            a (Point): First point.
            b (Point): Second point.

        Returns:
            float: Euclidean distance between points a and b.
        """
        deltas = a.coordinate - b.coordinate
        return float(np.linalg.norm(deltas))

    def total_distance(self) -> float:
        """Calculates the total distance traveled by the route in current order.

        Sums the Euclidean distance between each pair of consecutive points,
        in the order they were provided to RouteCalculator.

        Returns:
            float: Total distance in abstract meters. Returns 0.0 if the
                route has fewer than two points.
        """
        points = np.array([p.coordinate for p in self._points])
        if len(points) < 2:
            return 0
        deltas = points[1:] - points[:-1]
        distance = np.sqrt(np.sum(deltas**2, axis=1))
        return float(np.sum(distance))

    def nearest_neighbor(self) -> list[Point]:
        """Applies the nearest neighbor algorithm to optimize the route.

        Starts from the first point and iteratively selects the unvisited
        point closest to the current point until all points are visited.

        Returns:
            list[Point]: List of points reordered according to the nearest
                neighbor algorithm.

        Raises:
            ValueError: If the point list is empty.
        """
        unvisited = self.points
        if not unvisited:
            raise ValueError("Lista não pode estar vazia")
        current = unvisited.pop(0)
        route = [current]
        while unvisited:
            minimum = min(unvisited, key= lambda point: self.distance_between(current, point))
            unvisited.remove(minimum)
            route.append(minimum)
            current = minimum
        return route