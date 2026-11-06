import numpy
import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass
class Cube:
    side_length: float
    mass: float

    def __post_init__(self):
        self.volume = self.side_length ** 3
        self.density = self.mass / self.volume
        self.surface_area = (self.side_length ** 2) * 6

    def __str__(self):
        return (f"Cube Dimensions & Properties:\n"
                f"  Side Length:  {self.side_length}\n"
                f"  Mass:         {self.mass}\n"
                f"  Volume:       {self.volume}\n"
                f"  Density:      {self.density}\n"
                f"  Surface Area: {self.surface_area}")


my_cube = Cube(side_length=2.0, mass=16.0)
print(my_cube)
