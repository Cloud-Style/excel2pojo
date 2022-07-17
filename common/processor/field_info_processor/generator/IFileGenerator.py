class IFileGenerator:
    def generate(self,
                 package_name: str,
                 class_name: str,
                 field_info_list: list,
                 config_metadata: dict):
        """
        根据包名、类名、转换后的字段列表、配置信息来生成POJO对象

        :param package_name 包名
        :param class_name 类名
        :param field_info_list 字段信息列表
        :param config_metadata 配置信息
        """
        pass
