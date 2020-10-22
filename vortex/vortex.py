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
        self.vortices_unid = []  # Unidentified vortices
        self.vortices_sqv = []
        self.vortices_hqv = []

    def add_vortex(self, vortex):
        # * If vortex type is identified, add it to appropriate list; otherwise add to unid list
        if vortex.type is None:
            self.vortices_unid.append(vortex)
        elif vortex.type == 'SQV':
            self.vortices_sqv.append(vortex)
        elif vortex.type == 'HQV':
            self.vortices_hqv.append(vortex)
        else:
            raise AttributeError('Vortex does not have a valid type.')

    def num_of_vortices(self):
        print('There are {} SQVs and {} HQVs in the system.'.format(len(self.vortices_sqv), len(self.vortices_hqv)))
        return len(self.vortices_sqv) + len(self.vortices_hqv)

    def identify_vortices(self, threshold):
        # * Finds SQVs by finding overlapping vortices in the components
        # * Threshold determines the maximum distance between to cores to be classed as a SQV

        vortices_plus = [vortex for vortex in self.vortices_unid if vortex.component == 'plus']
        vortices_minus = [vortex for vortex in self.vortices_unid if vortex.component == 'minus']

        for vortex_plus in vortices_plus:
            for vortex_minus in vortices_minus:
                if abs(vortex_plus.x - vortex_minus.x) < threshold:
                    if abs(vortex_plus.y - vortex_minus.y) < threshold:
                        # * If this evaluates to true, the two vortices are within the threshold
                        # * So update the map with an SQV object taking an average position of both vortices

                        sqv = Vortex(((vortex_plus.x + vortex_minus.x) / 2,
                                      (vortex_plus.y + vortex_minus.y) / 2), vortex_plus.winding, 'both')
                        sqv.update_type('SQV')
                        self.add_vortex(sqv)

                        vortex_plus.update_type('SQV')
                        vortex_minus.update_type('SQV')

        # * Determines HQVs by setting all remaining unidentified vortices to HQVs
        for vortex in self.vortices_unid:
            if vortex.type is None:
                vortex.update_type('HQV')
                vortex.update_uid()
                self.add_vortex(vortex)
                self.vortices_unid.remove(vortex)
