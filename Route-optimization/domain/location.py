import numpy as np

class Point:
    """Represents an immutable point in 2D space.

    This class encapsulates x and y coordinates as immutable data,
    ensuring that values are valid finite numbers.
    """

    def __init__(self, x: float, y: float):
        """Initializes a Point with x and y coordinates.

        Args:
            x (float): X coordinate of the point. Must be a finite number.
            y (float): Y coordinate of the point. Must be a finite number.

        Raises:
            ValueError: If x or y are NaN or infinite.
        """
        if not np.isfinite(x):
            raise ValueError("X não pode ser NaN ou infinito")
        if not np.isfinite(y):
            raise ValueError("Y não pode ser NaN ou infinito")
        self._point = np.array([x, y], dtype=np.float64)

    @property
    def coordinate(self):
        """Returns the point coordinates as a numpy array.

        Returns:
            numpy.ndarray: Array of shape (2,) containing the coordinates [x, y].
        """
        return self._point

    