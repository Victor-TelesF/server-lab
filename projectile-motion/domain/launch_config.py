class LaunchConfig:
    def __init__(self, v0: float, angle_deg: float, gravity: float):

        if v0 <= 0:
            raise ValueError("Velocidade inicial não pode ser menor que 0")
        self._v0 = v0
        if angle_deg < 0 or angle_deg > 90:
            raise ValueError("Ángulo tem que estar entre 0 e 90 graus")
        self._angle_deg = angle_deg
        if gravity <= 0:
            raise ValueError("Gravidade não pode ser 0 ou negativa")
        self._gravity = gravity

    @property
    def v0(self) -> float:
        return self._v0

    @property
    def angle_deg(self) -> float:
        return self._angle_deg

    @property
    def gravity(self) -> float:
        return self._gravity