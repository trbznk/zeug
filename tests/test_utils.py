import zeug


def test_sin_cos_transformation():
    a = [0, 1, 2, 3, 4, 5, 6]
    period = 7

    a_sin, a_cos = zeug.sin_cos_transformation(a, period=period)

    assert a_sin.shape == a_cos.shape
