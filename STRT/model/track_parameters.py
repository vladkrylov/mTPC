def _calc_length(track):
    pass

def _calc_phi(track):
    pass

def _calc_D0(track):
    pass

def _calc_nhits(track):
    pass

def _calc_hits_min_dist(track):
    pass

def calculate_track_parameters(tracks):
    for t in tracks:
        for p in track_params_dict:
            t.parameters[p] = track_params_dict[p](t)
        
track_params_dict = {"Length": _calc_length,
                     "Phi": _calc_phi,
                     "D0": _calc_D0,
                     "Nhits": _calc_nhits,
                     "Dmin": _calc_hits_min_dist}

