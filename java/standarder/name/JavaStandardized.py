from common.processor.field_info_processor.standardized.processor.name.IStandardized import IStandardized
from common.util import FieldNameUtil, CommonUtil


class JavaStandardized(IStandardized):

    def convert(self, field_name_str: str):
        if CommonUtil.is_none_or_nan(field_name_str):
            return field_name_str

        # 变为驼峰形式
        return FieldNameUtil.to_hump(field_name_str)
