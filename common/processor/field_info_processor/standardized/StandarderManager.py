class IStandardizedManager:
    """
    标准化器
    """

    def standard_name(self, name: str):
        """
        标准化字段名

        用于将设计文档中 person_name或者personName 转换为对应语言要求的字段命名格式

        以java为例，Java要求驼峰格式，所以会将剪贴板中的下划线形式转为驼峰
        person_name -> personName

        :param name:
        :return:
        """
        pass

    def standard_type(self, type: str):
        """
        标准化字段类型

        将str, string 转换为各语言自己的标准名称，以Java为例

        str, string, String -> String
        int, Int, integer, Integer -> Integer

        :param type:
        :return:
        """
        pass
