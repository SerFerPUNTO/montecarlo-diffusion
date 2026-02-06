from random_walk import RandomWalk
import numpy as np

def main():

    sim = RandomWalk(
        grid_dim=[50, 50],
        n_particles=10000,
        steps=10000,
        seed=1,
    )
    sim.run(10)

main()