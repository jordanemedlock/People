
from radarfactory import radar_factory
import matplotlib.pyplot as plt
import numpy as np


def spiderplot(filename, names, values, frame='circle'):
    n = len(names)
    assert n == len(values)
    theta = radar_factory(n, frame=frame)
    fig, ax = plt.subplots(figsize=(9,9), nrows=1, ncols=1,
        subplot_kw={'projection':'radar'})
    ax.set_rgrids([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.plot(theta, values, color='b')
    ax.fill(theta, values, facecolor='b', alpha=0.25)
    ax.set_varlabels(names)
    plt.savefig(filename)

def vectorplot(filename, names, values, colors='k'):
    fig, ax = plt.subplots(figsize=(9,9), nrows=1, ncols=1)
    U, V = zip(*values)
    X, Y = zip(*[(0.0,0.0) for _ in names ])
    if not isinstance(colors, list):
        colors = [ colors for _ in names ]
    U = np.array(U, dtype=np.float64)
    V = np.array(V, dtype=np.float64)
    X = np.array(X, dtype=np.float64)
    Y = np.array(Y, dtype=np.float64)
    print(np.all(np.isfinite(U)), np.all(np.isfinite(V)), np.all(np.isfinite(X)), np.all(np.isfinite(Y)))
    ax.quiver(U, V, X, Y, angles='xy', scale_units='xy', scale=1, pivot='tail')

    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
    plt.savefig(filename)


