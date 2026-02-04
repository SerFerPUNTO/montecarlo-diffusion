from random_walk import RandomWalk
import numpy as np

def main():

    grid_dim = 500
    n_particles = 100000

    start_pos = np.zeros(grid_dim, dtype=int)

    start_pos[0] = n_particles // 2
    start_pos[-1] = n_particles - start_pos[0]

    sim = RandomWalk(
        grid_dim=500,
        n_particles=100000,
        steps=10000,
        seed=1,
        start_pos=start_pos
    )
    sim.run(100)

main()