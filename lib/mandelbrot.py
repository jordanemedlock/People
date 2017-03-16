
from capability import Capability
import numpy as np
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt

class Mandelbrot(Capability):
    def __init__(self, person=None):
        Capability.__init__(self, person)

    def mandelbrot_set(self, xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
        X = np.linspace(xmin, xmax, xn, dtype=np.float32)
        Y = np.linspace(ymin, ymax, yn, dtype=np.float32)
        C = X + Y[:,None]*1j
        N = np.zeros(C.shape, dtype=int)
        Z = np.zeros(C.shape, np.complex64)
        for n in range(maxiter):
            print('iteration:', n)
            I = np.less(abs(Z), horizon)
            N[I] = n
            Z[I] = Z[I]**2 + C[I]
        N[N==maxiter-1] = 0
        return Z, N

    def plot(self, filename):

        loglog2 = lambda n: np.log(np.log(n))/np.log(2)

        xmin, xmax, xn = -3.0, +3.0, 6000
        ymin, ymax, yn = -3.0, +3.0, 6000

        maxiter = 200
        horizon = 2.0 ** 40
        log_horizon = loglog2(horizon)
        print('Calculating set')
        Z, N = self.mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)

        with np.errstate(invalid='ignore'):
            M = np.nan_to_num(N + 1 - loglog2(Z) + log_horizon)

        dpi = 72
        width = 20
        height = 20*yn/xn
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

        print('saving image')
        plt.imshow(np.absolute(M), extent=[xmin, xmax, ymin, ymax], interpolation='bicubic', cmap='Set1')
        ax.set_xticks([])
        ax.set_yticks([])

        plt.savefig(filename)
        print('image saved')

if __name__ == '__main__':
    mandelbrot = Mandelbrot()
    mandelbrot.plot('mandelbrot.png')
