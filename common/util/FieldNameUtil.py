def to_under_line(name: str):
    """
    将名称变为下划线格式

    :param name:
    :return:
    """
    if not name:
        return None

    res = ''

    for i in name:
        if i.isupper():
            res += "_" + i.lower()
        else:
            res += i

    return res


def to_hump(name: str):
    """
    将名称变为驼峰格式

    :param name:
    :return:
    """
    if not name:
        return None

    res = ''

    pre_is_underline = False

    for i in name:
        if i != '_':
            if pre_is_underline:
                res += i.upper()
            else:
                res += i

            pre_is_underline = False
        else:
            pre_is_underline = True

    return res