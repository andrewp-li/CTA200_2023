import numpy as np

def f(z0,c,epsilon,max_iter):
    for i in range(max_iter):
        z1 = z0**2 + c #iterate
        if np.abs(z1) > 2: #met criteria for divergence
            return i
        else: #update
            z0 = z1
    return np.nan #converges

def complex_iterate(N=100,z0=0,epsilon=1e-4,max_iter=1000):
    '''Iterates method of findign the roots of a function.
    
    Paramters:
    N - An integer. Creates NxN grid to sample points
    z0 - A float. The initial guess
    epsilon - A float. The tolerance
    max_iter - An integer. The maximum iterations
    
    Returns:
    2d numpy array. The coordinates of each is the number of iterations to converge, np.nan if divergent.
    '''
    arr = np.linspace(-2,2,N)
    re, im = np.meshgrid(arr,arr*1j)
    c = re + im
    return [[f(z0,c[i][j],epsilon,max_iter) for j in range(N)] for i in range(N)]