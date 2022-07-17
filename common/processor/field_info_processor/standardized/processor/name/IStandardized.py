class IStandardized:
    """
    字段名转换器，规范化字段名称
    用于将设计文档中 person_name或者personName 转换为对应语言要求的字段命名格式

    以java为例，Java要求驼峰格式，所以会将剪贴板中的下划线形式转为驼峰
    person_name -> personName
    """

    def convert(self, field_type_str):

        pass
