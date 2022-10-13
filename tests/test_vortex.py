from tracker.vortex import Vortex


class TestVortex:
    def test_instantiate_vortex(self):
        assert Vortex((0., 0.), 'sqv', 1)
