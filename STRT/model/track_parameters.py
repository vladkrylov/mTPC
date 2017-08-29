import math
import numpy as np

def _calc_length(track):
    x, y = track.line
    return math.sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2)


def _calc_phi(track):
    x, y = track.line
    if math.fabs(x[1] - x[0]) > 1e-9:
        return math.atan((y[1]-y[0]) / ((x[1]-x[0])))
    else:
        return None


def _calc_D0(track):
    return None


def _calc_nhits(track):
    return len(track.hit_indices)


def _calc_hits_min_dist(track):
    return None


def fit_track(track):
    if len(track.hit_indices):
        return None
    x = np.array(track.line[0])
    y = np.array(track.line[1])
    coeffs = np.polyfit(x, y, deg=1)
    
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    r2 = ssreg / sstot
    
    return coeffs, r2


def calculate_track_parameters(tracks):
    for t in tracks:
        for p in track_params_dict:
            t.parameters[p] = track_params_dict[p](t)
                    
        
track_params_dict = {"Length": _calc_length,
                     "Phi": _calc_phi,
                     "D0": _calc_D0,
                     "Nhits": _calc_nhits,
                     "Dmin": _calc_hits_min_dist}

