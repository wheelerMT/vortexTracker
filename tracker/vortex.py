import uuid
import numpy as np


class Vortex:
    """Contains the details about an individual vortex within the system."""

    def __init__(self, pos: tuple[float, float], vortex_type: str, winding: int | float):

        self._pos = pos
        self._type = vortex_type
        self._winding = winding
        self._uid = f'{self._type}_{uuid.uuid4()}'

    def position(self) -> tuple[float, float]:
        return self._pos

    def type(self):
        return self._type

    def winding(self):
        return self._winding

    def id(self) -> str:
        return self._uid

    def distance_to(self, vortex) -> float:
        vortex_pos = vortex.position()
        return np.sqrt((self._pos[0] - vortex_pos[0]) ** 2 + (self._pos[1] - vortex_pos[1]) ** 2)
