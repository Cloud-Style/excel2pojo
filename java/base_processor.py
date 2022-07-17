from common.processor.field_info_processor.field_info_reader import field_info_reader
from common.util import CommonUtil
from java.generator.JavaFileGenerator import JavaFileGenerator
from java.standarder.JavaStandardizedManager import JavaStandardizedManager


def read_field_list(df, field_index_config):
    """
    从剪贴板读取表格
    """

    return field_info_reader.parse_field_info(df, field_index_config)


def standard_field_data_list(field_list):
    """
    标准化字段数据
    :param field_list: 字段数据列表
    :return: 标准化后的字段
    """
    standardized_manager = JavaStandardizedManager()

    converted_field_list_res = []
    for item in field_list:
        if CommonUtil.is_none_or_nan(item) or CommonUtil.is_none_or_nan(item['field_name']):
            continue

        converted_item = {'field_name': standardized_manager.standard_name(item['field_name']),
                          'field_type': standardized_manager.standard_type(item['field_type']),
                          'field_commit': item['field_commit']}
        converted_field_list_res.append(converted_item)

    return converted_field_list_res


def generate(config_metadata, package_name, class_name, converted_field_list):
    """
    根据包名、类名、转换后的字段列表、配置信息来生成Java类
    :return:
    """

    java_file_generator = JavaFileGenerator()
    java_file_generator.generate(package_name, class_name, converted_field_list, config_metadata)
