import math


def is_none_or_nan(obj):
    if obj is None:
        return True

    if type(obj) is str:
        return not obj

    if type(obj) is float or type(obj) is int:
        return math.isnan(obj)
