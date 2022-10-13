import uuid


class Vortex:
    """Contains the details about an individual vortex within the system."""

    def __init__(self, pos: tuple[float, float], vortex_type: str, winding: int | float):

        self.pos = pos
        self.type = vortex_type
        self.winding = winding
        self.uid = f'{self.type}_{uuid.uuid4()}'
