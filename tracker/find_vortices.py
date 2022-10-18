import numpy as np
from tracker.vortex import Vortex, VortexMap


def find_vortices(wavefunction: np.ndarray, vortex_map: VortexMap, x_array, y_array) -> None:
    phase_x = np.unwrap(np.angle(wavefunction), axis=0)
    phase_y = np.unwrap(np.angle(wavefunction), axis=1)

    x_positions, y_positions = _find_low_density_points(wavefunction)

    for x_pos, y_pos in zip(x_positions, y_positions):
        # Check edge of box case
        if x_pos == wavefunction.shape[0] - 1:
            x_pos = -1
        if y_pos == wavefunction.shape[1] - 1:
            y_pos = -1

        phase_sum = _sum_plaquette(phase_x, phase_y, x_pos, y_pos)
        if np.round(abs(phase_sum), 4) == np.round(2 * np.pi, 4):
            if phase_sum > 0:
                vortex_map.add_vortex(Vortex((x_array[x_pos], y_array[y_pos]), 'sqv', -1))
            elif phase_sum < 0:
                vortex_map.add_vortex(Vortex((x_array[x_pos], y_array[y_pos]), 'sqv', 1))


def _find_low_density_points(wavefunction: np.ndarray):
    threshold = 0.3 * np.max(abs(wavefunction) ** 2)
    return np.where(abs(wavefunction) ** 2 < threshold)


def _sum_plaquette(phase_x, phase_y, x_pos, y_pos):
    phase_sum = 0
    phase_sum += phase_x[x_pos, y_pos + 1] - phase_x[x_pos, y_pos]
    phase_sum += phase_y[x_pos + 1, y_pos + 1] - phase_y[x_pos, y_pos + 1]
    phase_sum += phase_x[x_pos + 1, y_pos] - phase_x[x_pos + 1, y_pos + 1]
    phase_sum += phase_y[x_pos, y_pos] - phase_y[x_pos + 1, y_pos]

    return phase_sum

