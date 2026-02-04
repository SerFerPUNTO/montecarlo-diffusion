import numpy as np
import matplotlib as plt
from animated_grid import AnimatedGrid

class RandomWalk:
    def __init__(self, grid_dim, steps, n_particles, start_pos=None,seed=None):
        self.steps=steps
        self.seed=seed
        self.grid_dim=grid_dim
        self.n_particles=n_particles
        np.random.seed(self.seed)

        # initialize particles and grid
        if start_pos is None:
            if grid_dim%2==1:
                # one central cell
                center=grid_dim//2
                self.particles = np.ones(n_particles, dtype=int)*center
            else:
                # two central cells
                center1=grid_dim//2-1
                center2=grid_dim//2
                # distribute particles
                particles1=np.ones(n_particles//2, dtype=int)*center1
                particles2=np.ones(n_particles-n_particles//2, dtype=int)*center2
                self.particles = np.concatenate([particles1, particles2])
        else:
            start_pos = np.asarray(start_pos, dtype=int)
            if start_pos.size != grid_dim:
                raise ValueError("start_pos has different dimensions from grid_dim")
            n_particles = start_pos.sum()
            self.particles = np.repeat(np.arange(grid_dim), start_pos) # distribute particles

    def step(self, n):
        for _ in range(n):
            dx = np.random.randint(0, 2, size=self.n_particles)*2 - 1
            self.particles += dx
            np.clip(self.particles, 0, self.grid_dim-1, out=self.particles)
    
    def create_grid(self):
        self.grid = np.bincount(self.particles, minlength=self.grid_dim).reshape(1, -1)

    def run(self, plot_freq=None):
        if plot_freq is None:
            plot_freq=self.steps
        
        self.create_grid()
        anim=AnimatedGrid(self.grid)
        it=0
        while(it<self.steps):
            it+=plot_freq
            self.step(plot_freq)
            self.create_grid()
            anim.update(self.grid, it)
            
        anim.wait()
