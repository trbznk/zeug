import zeug
import numpy as np


def test_sin_cos_transformation():
    a = [0, 1, 2, 3, 4, 5, 6]
    period = 7

    a_sin, a_cos = zeug.sin_cos_transformation(a, period=period)

    assert a_sin.shape == a_cos.shape


def test_synth_ts():
    ts1 = zeug.synth_ts()
    ts2 = zeug.synth_ts(n=1000)
    ts3 = zeug.synth_ts(base=50, r_down=0, r_up=0)
    ts4 = zeug.synth_ts(base=30, r_down=0)

    assert type(ts1) == np.ndarray
    assert len(ts2) == 1000
    assert ts3[-1] == 50
    assert ts4[-1] > 30
