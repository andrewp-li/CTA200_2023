import numpy as np

def f(z0,c,max_iter):
    '''Iterate z_i+1=z^2+c until divergent
    
    Paramters:
    z0 - A complex number. The initial guess
    c - A complex number. The value of c to use
    max_iter - An integer. The maximum iterations
    
    Returns:
    An integer. The number of iterations to diverge, or np.nan if convergent.
    '''
    for i in range(max_iter):
        z1 = z0**2 + c #iterate
        if np.abs(z1) > 2: # criteria for divergence, return the iteration
            return i
        else: #update
            z0 = z1
    return np.nan #converges

def complex_iterate(N=100,z0=0,max_iter=1000):
    '''Applies f to a complex plane
    
    Paramters:
    N - An integer. Creates NxN grid to sample points
    z0 - A complex number. The initial guess
    max_iter - An integer. The maximum iterations
    
    Returns:
    2d numpy array. The coordinates of each is the number of iterations to diverge, np.nan if convergent.
    '''
    # Creating complex plane
    arr = np.linspace(-2,2,N)
    re, im = np.meshgrid(arr,arr*1j)
    c = re + im
    
    return [[f(z0,c[i][j],max_iter) for j in range(N)] for i in range(N)] # runs f for each point in the complex plane