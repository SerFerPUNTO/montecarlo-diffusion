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
        self.ax.set_yticks([])   # inutili in 1D
        self.ax.set_xticks([])   # COSTOSISSIMI se grid è grande

        plt.ion()
        plt.show(block=False)

    def update(self, grid, n_it=None):
        self.im.set_data(grid)

        # aggiorna colorbar SOLO se necessario
        self.im.set_clim(grid.min(), grid.max())

        if n_it is not None:
            self.ax.set_title(f"Iteration {n_it}")

        self.fig.canvas.draw_idle()
        self.fig.canvas.flush_events()
        plt.pause(self.pause)

    def wait(self):
            import matplotlib.pyplot as plt
            plt.ioff()
            plt.show(block=True)