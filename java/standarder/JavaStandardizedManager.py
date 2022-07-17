from common.processor.field_info_processor.standardized.StandarderManager import IStandardizedManager
from java.standarder.name.JavaStandardized import JavaStandardized as DefaultNameStandarder
from java.standarder.type import IntStandarder, StringStandarder
from java.standarder.type import ListStandarder, BoolStandarder, DoubleStandarder, FloatStandarder, DateStandarder, \
    DefaultObjectStandarder

field_name_standarder = DefaultNameStandarder()
field_type_standarder = [BoolStandarder.BoolStandarder(),
                         IntStandarder.IntStandarder(),
                         FloatStandarder.FloatStandarder(),
                         DoubleStandarder.DoubleStandarder(),
                         ListStandarder.ListStandarder(),
                         DateStandarder.DateStandarder(),
                         StringStandarder.StringStandarder(),
                         DefaultObjectStandarder.DefaultObjectStandarder()]


class JavaStandardizedManager(IStandardizedManager):
    def standard_name(self, name: str):
        return field_name_standarder.convert(name)

    def standard_type(self, field_type: str):
        for item in field_type_standarder:
            if item.isMatch(field_type):
                return item.convert(field_type)
