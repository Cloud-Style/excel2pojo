def is_blank(string: str) -> bool:
    """
    判断一个字符串是否为空串

    :param string:
    :return:
    """

    return string is None or len(string.strip(' ')) == 0