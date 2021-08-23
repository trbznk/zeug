import numpy as np


def sin_cos_transformation(a, period=None):
    a = np.array(a)

    if period is None:
        period = np.max(a)

    a_sin = np.sin((2*np.pi*a)/period)
    a_cos = np.cos((2*np.pi*a)/period)

    return a_sin, a_cos


def synth_ts(n=100, base=100, r_down=0.05, r_up=0.05):
    ts = np.array([])

    for t in range(n):
        r = np.random.uniform(low=1-r_down, high=1+r_up)
        base = base*r
        ts = np.append(ts, base)

    return ts


def sequence_ts(ts, window=2):
    assert len(ts) > 1, "ts must be larger than 1"
    assert window < len(ts) and window > 0, "0 < window < len(ts)"
    seqs = []
    for i in range(len(ts)-window+1):
        seqs.append(ts[i:i+window])
    return np.stack(seqs)
