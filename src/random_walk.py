import numpy as np
import matplotlib as plt
from animated_grid import AnimatedGrid

class RandomWalk:
    def __init__(self, grid_dim, steps, n_particles, start_pos=None,seed=None):
        self.steps=steps
        self.seed=seed
        self.grid_dim=tuple(grid_dim)
        self.n_particles=n_particles
        np.random.seed(self.seed)
        self.set_particles(start_pos=start_pos)

    def step(self, n):
        for _ in range(n):
            directions=np.random.randint(0, 4, size=self.n_particles)

            dx=np.zeros(self.n_particles, dtype=int)
            dy = np.zeros(self.n_particles, dtype=int)

            dx[directions==0]=1    # dx
            dx[directions==1]=-1   # sx
            dy[directions==2]=1    # up
            dy[directions==3]=-1   # down

            self.particles[0]+=dx
            self.particles[1]+=dy

            np.clip(self.particles[0], 0, self.grid_dim[0]-1, out=self.particles[0])
            np.clip(self.particles[1], 0, self.grid_dim[1]-1, out=self.particles[1])

    
    def create_grid(self):
        nx, ny=self.grid_dim

        # create 1d index
        lin_idx=self.particles[0]*ny+self.particles[1]

        self.grid=np.bincount(
            lin_idx,
            minlength=nx*ny
        ).reshape(nx, ny)

        #same as:
        #for i in range(self.n_particles):
        #    x = self.particles[0, i]
        #    y = self.particles[1, i]
        #    grid[x, y] += 1



    def run(self, plot_freq=None):
        if plot_freq is None:
            plot_freq=self.steps
        
        self.create_grid()
        anim=AnimatedGrid(self.grid, pause=0.001)
        it=0
        while(it<self.steps):
            n = min(plot_freq, self.steps - it)
            it+=plot_freq
            self.step(n)
            self.create_grid()
            anim.update(grid=self.grid, n_it=it)
            
        anim.wait()
    
    def set_particles(self, start_pos):
        # initialize particles
        if start_pos is None:
            self.particles=np.zeros((2,self.n_particles), dtype=int)

            if self.grid_dim[0]%2==1:
                cx=self.grid_dim[0]//2
                self.particles[0, :]=cx
            else:
                k=self.n_particles//2
                cx1=self.grid_dim[0]//2-1
                cx2=self.grid_dim[0]//2
                self.particles[0, :k]=cx1
                self.particles[0, k:]=cx2

            if self.grid_dim[1]%2==1:
                cy=self.grid_dim[1]//2
                self.particles[1, :]=cy
            else:
                k=self.n_particles//2
                cy1=self.grid_dim[1]//2-1
                cy2=self.grid_dim[1]//2
                self.particles[1, :k]=cy1
                self.particles[1, k:]=cy2
        else:
            start_pos = np.asarray(start_pos, dtype=int)

            if start_pos.shape != tuple(self.grid_dim):
                raise ValueError("start_pos has different dimensions from grid_dim")

            if start_pos.sum() != self.n_particles:
                raise ValueError("start_pos has different number of particles from n_particles")

            xs, ys = np.indices(self.grid_dim)
            self.particles = np.vstack([
                np.repeat(xs.ravel(), start_pos.ravel()),
                np.repeat(ys.ravel(), start_pos.ravel())
            ]) # distribute particles
