from common.processor.field_info_processor.standardized.processor.type.Standarder import Standarder
from common.util import CommonUtil


class DefaultObjectStandarder(Standarder):

    def isMatch(self, field_type_str: str):
        if CommonUtil.is_none_or_nan(field_type_str):
            return True

    def convert(self, field_type_str: str):
        return 'Object'
