from abc import ABC

from math import pi, cos, sin
from .launch_config import LaunchConfig


class Engine(ABC):
    def __init__(self, config: LaunchConfig):
        self._config = config

    @property
    def config(self) ->LaunchConfig:
        return self._config
    
    @property
    def angle_rad(self) -> float:
        return (self.config.angle_deg * (pi/180))
    
    @property
    def v0x(self):
        return (self.config.v0 * cos(self.angle_rad))
        
    @property
    def v0y(self):
        return self.config.v0 * sin(self.angle_rad)

    