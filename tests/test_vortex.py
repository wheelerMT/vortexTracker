import pytest
from tracker.vortex import Vortex


@pytest.fixture
def vortex():
    return Vortex((0., 0.), 'sqv', 1)


class TestVortex:
    def test_instantiate_vortex(self, vortex):
        assert vortex is not None

    def test_position(self, vortex):
        assert vortex.position() == (0., 0.)

    def test_type(self, vortex):
        assert vortex.type() == 'sqv'

    def test_winding(self, vortex):
        assert vortex.winding() == 1

    def test_uid(self, vortex):
        assert vortex.id() is not None

    @pytest.mark.parametrize("vortex_positions, expected_result",
                             [((3., 4.), 5.), ((0., 0.), 0.), ((-5., 12.), 13.)])
    def test_distance_to(self, vortex, vortex_positions, expected_result):
        other_vortex = Vortex(vortex_positions, 'sqv', 1)
        assert vortex.distance_to(other_vortex) == expected_result

    def test_update_position(self, vortex):
        vortex.update_position((1., -5.))
        assert vortex.position() == (1., -5.)
