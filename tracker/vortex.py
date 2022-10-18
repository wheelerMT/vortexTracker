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

    def type(self) -> str:
        return self._type

    def winding(self) -> int:
        return self._winding

    def id(self) -> str:
        return self._uid

    def distance_to(self, vortex) -> float:
        vortex_pos = vortex.position()
        return np.sqrt((self._pos[0] - vortex_pos[0]) ** 2 + (self._pos[1] - vortex_pos[1]) ** 2)

    def closest_vortex(self, vortex_map):
        pass

    def update_position(self, pos: tuple[float, float]) -> None:
        self._pos = pos


class VortexMap:
    """Map that contains all the vortices within the system."""

    def __init__(self):
        self.map = {}

    def add_vortex(self, vortex) -> None:
        """Adds a vortex to the map.
        :param vortex: the vortex object.
        """
        self.map[vortex.id()] = vortex

    def remove_vortex(self, vortex) -> None:
        """Removes a vortex from the map.
        :param vortex: The vortex object.
        """
        del self.map[vortex.id()]
