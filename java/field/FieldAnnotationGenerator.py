class FieldAnnotationGenerator:
    def is_open(self, config_metadata: dict):
        """
        是否开启本generator，true表示开启

        :param config_metadata: 配置
        :return:
        """
        pass

    def generate(self, config_metadata: dict, class_package_list: list, field_info: dict) -> list:
        """
        生产

        :param config_metadata: 配置信息
        :param class_package_list: 类包信息
        :param field_info: 字段信息
        :return:
        """
        pass
