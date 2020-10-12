import numpy as np
import uuid


class Vortex:
    """ Vortex class to categorize vortices within a spinor BEC."""
    def __init__(self, position, winding, component):
        self.x, self.y = position
        self.winding = winding
        self.type = None  # String: type of vortex (i.e. SQV or HQV)
        self.uid = uuid.uuid1()  # Unique identifier: Gets initialised and updated to reflect type of vortex later
        self.isTracked = True   # Tracking argument for vortex
        self.component = component  # Which component of the wavefunction the vortex is in

    def get_coords(self):
        return self.x, self.y

    def get_uid(self):
        return self.uid

    def get_v_type(self):
        return self.type

    def get_distance(self, vortex):  # Calculate distance between two vortices:
        return np.sqrt((self.x - vortex.x) ** 2 + (self.y - vortex.y) ** 2)

    def update_type(self, vortex_type):
        self.type = vortex_type

    def update_uid(self):
        self.uid = '{}_{}'.format(self.type, self.uid)

    def update_coords(self, pos_x, pos_y):
        self.x, self.y = pos_x, pos_y


class VortexMap:
    """Map that keeps track of all vortices within a condensate."""
    def __init__(self):
        self.vortices = []

    def add_vortex(self, vortex):
        self.vortices.append(vortex)

    def num_of_vortices(self):
        return len(self.vortices)

    def find_SQVs(self, threshold):
        # * Finds SQVs by finding overlapping vortices in the components
        # * Threshold determines the maximum distance between to cores to be classed as a SQV

        checked_list = []
        for vortex1 in self.vortices:
            for vortex2 in self.vortices:
                if vortex1 == vortex2 or vortex1 in checked_list:
                    continue
                if abs(vortex1.x - vortex2.x) < threshold:
                    if abs(vortex1.y - vortex2.y) < threshold:
                        # * If this evaluates to true, the two vortices are too close together
                        # * So remove vortex1 and update the type and uid of vortex2

                        if vortex1 in self.vortices:
                            self.vortices.remove(vortex1)
                        vortex2.update_type('SQV')
                        vortex2.update_uid()
                        checked_list.append(vortex2)

    def find_HQVs(self):
        # ! find_SQVs has to be called before this method to ensure accuracy!
        # * Determines HQVs by setting all remaining unidentified vortices to HQVs
        for vortex in self.vortices:
            if vortex.type is None:
                vortex.update_type('HQV')
                vortex.update_uid()

    def compare_maps(self, tempMap, threshold):
        # * Compares the master map with the temp map to determine which vortices to update

        for masterVortex in self.vortices:
            for tempVortex in tempMap.vortices:
                if masterVortex.get_distance(tempVortex) < threshold:
                    masterVortex.x, masterVortex.y = tempVortex.get_coords()

        for remaining_vortex in tempMap.vortices:
            # * Adds remaining vortices to master map
            # ? Main use is for adding new HQVs into master map from splitting SQVs
            self.add_vortex(remaining_vortex)
