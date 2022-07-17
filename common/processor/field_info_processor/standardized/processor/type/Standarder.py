class Standarder:
    """
    字段类型标准化器，将str, string 转换为各语言自己的标准名称，以Java为例

    str, string, String -> String
    int, Int, integer, Integer -> Integer

    """

    def isMatch(self, field_type_str):
        """
        是否匹配当前标准化器

        :param field_type_str:
        :return:
        """
        pass

    def convert(self, field_type_str):
        """
        使用当前标准化器进行转换

        :param field_type_str:
        :return:
        """
        pass
