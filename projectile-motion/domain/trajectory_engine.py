from .launch_config import LaunchConfig
from .engine import Engine

class TrajectoryEngine(Engine):
    def __init__(self, config: LaunchConfig):
        super().__init__(config)

    @staticmethod
    def _validate_time(time: float) -> None:
        if time < 0:
            raise ValueError("Tempo não pode ser negativo")

    def gravity_drop(self, time: float) -> float:
        self._validate_time(time)
        return ((self.config.gravity * (time**2))/2)

    def horizontal_position(self, time: float) -> float:
        self._validate_time(time)
        return (self.v0x * time)

    def vertical_position(self, time: float) -> float:
        self._validate_time(time)
        return ((self.v0y * time) - self.gravity_drop(time))

    def position_at(self, time: float) -> tuple[float, float]:
        x = self.horizontal_position(time)
        y = self.vertical_position(time)
        return x, y

    def max_height(self) -> tuple[float, float]:
        time_at_peak = self.v0y / self.config.gravity
        height = self.vertical_position(time_at_peak)
        return time_at_peak, height

    def time_of_flight(self) -> float:
        total_time = 2 * (self.v0y / self.config.gravity)
        return total_time

    def trajectory_points(self, num_points: int) -> list[dict[str, float]]:
        if num_points <= 0:
            raise ValueError("Número de pontos deve ser maior que 0")
        
        t_flight = self.time_of_flight()
        points = []
        for i in range(num_points + 1):
            t = t_flight * i / num_points
            x, y = self.position_at(t)
            points.append({"t": t, "x": x, "y": y})
        return points