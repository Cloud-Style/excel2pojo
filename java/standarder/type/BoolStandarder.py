from common.util import CommonUtil
from common.processor.field_info_processor.standardized.processor.type.Standarder import Standarder


class BoolStandarder(Standarder):
    type_tag = ("bool", "boolean")
    standard_field_type_name = "Boolean"

    def isMatch(self, field_type_str: str):
        if CommonUtil.is_none_or_nan(field_type_str):
            return False

        return field_type_str.lower() in self.type_tag

    def convert(self, field_type_str: str):
        return self.standard_field_type_name
