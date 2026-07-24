import math

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("Positive numbers expected")
        self._radius = value
