import numpy as np
def x_sec_area(D):
    """Cross-sectional area of a uniform pipe

    Keyword arguments:
    D -- internal diameter (m)
     
    """
    if np.any(D <=0):
        raise ValueError("Non-positive internal pipe diam.")
    return np.pi * np.power((0.5 * D), 2)

