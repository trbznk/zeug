import zeug
import numpy as np
import pytest


def test_sin_cos_transformation():
    a = [0, 1, 2, 3, 4, 5, 6]
    period = 7
    a_sin, a_cos = zeug.sin_cos_transformation(a, period=period)
    assert a_sin.shape == a_cos.shape


def test_synth_ts():
    ts = zeug.synth_ts()
    assert type(ts) == np.ndarray

    ts = zeug.synth_ts(n=1000)
    assert len(ts) == 1000

    ts = zeug.synth_ts(base=50, r_down=0, r_up=0)
    assert ts[-1] == 50

    ts = zeug.synth_ts(base=30, r_down=0)
    assert ts[-1] > 30
    

def test_sequence_ts():
    ts = np.random.rand(100)
    seqs = zeug.sequence_ts(ts)
    assert type(ts) == np.ndarray

    ts = np.array([1, 2, 3, 4, 5, 6])
    seqs = zeug.sequence_ts(ts, window=2)
    assert seqs.shape == (5, 2)

    ts = np.array([1, 2, 3, 4, 5, 6])
    seqs = zeug.sequence_ts(ts, window=4)
    assert seqs.shape == (3, 4)

    ts = np.array([1, 2, 3, 4, 5, 6])
    seqs = zeug.sequence_ts(ts, window=2)
    assert np.array_equal(seqs[-1], np.array([5, 6]))

    ts = np.array([1])
    with pytest.raises(AssertionError) as excinfo:
        zeug.sequence_ts(ts)
    assert "ts must be larger than 1" in str(excinfo.value)

    ts = np.array([1, 2, 3, 4, 5])
    with pytest.raises(AssertionError) as excinfo:
        zeug.sequence_ts(ts, window=-22)
        zeug.sequence_ts(ts, window=5)
    assert "0 < window < len(ts)" in str(excinfo.value)

    ts = [1, 2, 3, 4, 5]
    zeug.sequence_ts(ts)
    