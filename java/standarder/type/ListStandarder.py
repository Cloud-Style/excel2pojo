from common.processor.field_info_processor.standardized.processor.type.Standarder import Standarder
from common.util import CommonUtil


class ListStandarder(Standarder):
    type_tag = ("list", "array", "arr")
    standard_field_type_name = "List"

    def isMatch(self, field_type_str: str):
        if CommonUtil.is_none_or_nan(field_type_str):
            return False

        return field_type_str.lower() in self.type_tag

    def convert(self, field_type_str: str):
        return self.standard_field_type_name
