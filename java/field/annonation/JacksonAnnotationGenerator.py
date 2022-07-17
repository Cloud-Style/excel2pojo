from common.util import FieldNameUtil, StrUtil, CommonUtil
from java.field.FieldAnnotationGenerator import FieldAnnotationGenerator
from java.standarder.type.DateStandarder import DateStandarder


class JacksonAnnotationGenerator(FieldAnnotationGenerator):
    def is_open(self, config_metadata: dict):
        """
        是否开启本generator，true表示开启

        :param config_metadata: 配置
        :return:
        """
        return config_metadata.get('jackson', {}).get('enable')

    def generate(self, config_metadata: dict, class_package_set: set, field_info: dict) -> list:
        """
        生产

        :param class_package_set:
        :param config_metadata: 配置信息
        :param field_info: 字段信息
        :return:
        """
        res_list = []
        JacksonAnnotationGenerator.process_alias(config_metadata, class_package_set, field_info, res_list)
        JacksonAnnotationGenerator.process_property(config_metadata, class_package_set, field_info, res_list)
        JacksonAnnotationGenerator.process_date_format(config_metadata, class_package_set, field_info, res_list)

        return res_list

    @staticmethod
    def process_alias(config_metadata, class_package_set: set, field_info, res_list):
        if config_metadata.get('jackson', {}).get('alias.enable', False) is True:
            class_package_set.add("import com.fasterxml.jackson.annotation.JsonAlias;")

            under_line_field_name = FieldNameUtil.to_under_line(field_info['field_name'])
            field_name_hump = FieldNameUtil.to_hump(field_info['field_name'])

            if StrUtil.is_blank(under_line_field_name):
                return

            if under_line_field_name == field_name_hump:
                res_list.append(f"""@JsonAlias("{under_line_field_name}")""")
            else:
                res_list.append(f"""@JsonAlias({{"{under_line_field_name}", "{field_name_hump}"}})""")

    @staticmethod
    def process_property(config_metadata, class_package_set: set, field_info, res_list):
        if config_metadata.get('jackson', {}).get('property.enable', False) is True:
            class_package_set.add("import com.fasterxml.jackson.annotation.JsonProperty;")

            under_line_field_name = FieldNameUtil.to_under_line(field_info['field_name'])
            if StrUtil.is_blank(under_line_field_name):
                return

            res_list.append(f"""@JsonProperty("{under_line_field_name}")""")

    @staticmethod
    def process_date_format(config_metadata, class_package_set, field_info, res_list):
        if config_metadata.get('jackson', {}).get('dateformat.enable', False) is True:
            class_package_set.add("import com.fasterxml.jackson.annotation.JsonFormat;")

            if CommonUtil.is_none_or_nan(field_info['field_type']):
                return

            if field_info['field_type'] == DateStandarder.standard_field_type_name:
                res_list.append("""@JsonFormat(pattern = "yyyy-MM-dd", timezone = "GMT+8")""")

