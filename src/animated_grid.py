import matplotlib.pyplot as plt

class AnimatedGrid:
    def __init__(self, grid, pause=0.001):
        self.pause = pause

        self.fig, self.ax = plt.subplots()
        self.im = self.ax.imshow(
            grid,
            cmap="viridis",
            interpolation="nearest",
            aspect="auto",
            animated=True
        )

        self.cbar = self.fig.colorbar(self.im, ax=self.ax)
        self.ax.set_yticks([])
        self.ax.set_xticks([])

        # scatter opzionale per particelle
        self.scatter = self.ax.scatter([], [], c='red')

        plt.ion()
        plt.show(block=False)

    def update(self, grid=None, particles=None, n_it=None):
        if grid is not None:
            self.im.set_data(grid)
            vmin, vmax = grid.min(), grid.max()
            if vmin == vmax:
                vmax = vmin + 1
            self.im.set_clim(vmin, vmax)

        if particles is not None:
            self.scatter.set_offsets(particles.T)

        if n_it is not None:
            self.ax.set_title(f"Iteration {n_it}")
        else:
            self.ax.set_title("")

        self.fig.canvas.draw_idle()
        self.fig.canvas.flush_events()
        plt.pause(self.pause)

    def wait(self):
        plt.ioff()
        plt.show(block=True)
