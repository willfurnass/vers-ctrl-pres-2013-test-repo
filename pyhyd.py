import numpy as np
def x_sec_area(D):
    """Cross-sectional area of a uniform pipe

    Keyword arguments:
    D -- internal diameter (m)
     
    """
    return np.pi * np.power((0.5 * D), 2)

