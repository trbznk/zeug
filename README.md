# ZEUG

### Installation

```bash
pip install zeug
```

### Tranform cyclical data

Assume you have cyclical data like weekday. `0` for monday and `6` for sunday. Even the difference between sunday and monday is only 1 day the numerical difference between `0` and `6` is big.

```python
weekdays = [0, 1, 2, 3, 4, 6]
```

We can use sinus and cosinus tranformation to preprocess cyclical data like `hours`, `weekdays` and `months`.

```python
weekdays_sin, weekdays_cos = zeug.sin_cos_transformation(weekdays, period=7)
```

The result consists of the sinus and cosinus values that hold the information about the cyclical behavior.

![sin_cos_tranformation() example](./bin/sin_cos_tranformation.png)
