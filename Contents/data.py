import numpy as np

def extract_halo(haloid_path):
    ndout = np.load(haloid_path)
    return ndout

def set_lw(cutoff, ndin):
    ndin[np.where(ndin < cutoff)] = 0
    return ndin


