from vortex import Vortex


class VortexMap:
    """Map that contains all the vortices within the system."""

    def __init__(self):
        self.map = {}

    def add_vortex(self, vortex: Vortex) -> None:
        """Adds a vortex to the map.
        :param vortex: the vortex object.
        """
        self.map[vortex.uid] = vortex

    def remove_vortex(self, uid: str) -> None:
        """Removes a vortex from the map.
        :param uid: unique ID of the vortex.
        """
        # ? Should this take a vortex object instead?
        del self.map[uid]
