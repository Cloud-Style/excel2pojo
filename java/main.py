import datetime

import pandas

from common.util import CommonUtil
from java import base_processor

if __name__ == '__main__':
    # 类名，无需带.java后缀
    class_name = 'Tmp'
    field_index_config = {
        # 字段名在excel中列的索引，从0开始计数
        'field_name_index': 0,
        # 字段类型在excel中列的索引，从0开始计数
        'field_type_index': 1,
        # 字段注释在excel中的列索引，从0开始计数
        "field_mean_index": 4
    }

    package_name = 'com.test'
    print('package_name = {}', package_name)

    """
    1. 读取数据
    """
    # 从剪贴板读取数据
    df = pandas.read_clipboard()
    print(df)
    # 从excel读取数据
    # df = pandas.read_excel('')

    field_data_list = base_processor.read_field_list(df, field_index_config)
    print('field_data_list = {}'.format(field_data_list))

    """
    2. 过滤数据名称前缀，
    比如表格的数据都是
    data.nodes[].data.id
    data.nodes[].data.name
    
    我想去掉前缀 data.nodes[].data. 
    只保留 id name
    那么可以在这里配置
    """
    for field_data in field_data_list:
        if CommonUtil.is_none_or_nan(field_data['field_name']):
            continue
        field_data['field_name'] = field_data['field_name'].removeprefix("+")
        field_data['field_name'] = field_data['field_name'].removeprefix(".")

    """
    3. 标准化各个字段类型
    """
    converted_field_list = base_processor.standard_field_data_list(field_data_list)
    print('converted_field_list = {}'.format(converted_field_list))

    """
    4. 配置元信息
    目前可以配置的都在下面列出了
    """
    config_metadata = {
        # 当前作者名称
        'author': 'majie15',
        # 文件编写日期，默认今天
        'date': datetime.date.today().isoformat(),
        # jackson
        'jackson': {
            'enable': True,
            'alias.enable': True,
            'property.enable': True,
            'dateformat.enable': True
        }
    }

    """
    5. 生成
    """
    base_processor.generate(config_metadata, package_name, class_name, converted_field_list)
