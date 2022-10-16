from tracker.vortex import Vortex, VortexMap


class TestVortexMap:
    def test_instantiate_vortex_map(self):
        assert VortexMap() is not None

    def test_add_vortex(self):
        vortex_map = VortexMap()
        vortex = Vortex((0., 0.), 'sqv', 1)
        vortex_map.add_vortex(vortex)

        assert vortex.id() in vortex_map.map

    def test_remove_vortex(self):
        vortex_map = VortexMap()
        vortex = Vortex((0., 0.), 'sqv', 1)
        vortex_map.add_vortex(vortex)
        vortex_map.remove_vortex(vortex)

        assert vortex.id() not in vortex_map.map
