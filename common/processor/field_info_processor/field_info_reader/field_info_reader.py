from pandas import DataFrame


def parse_field_info(df: DataFrame, field_index_config: dict) -> list[dict]:
    """
    读取数据
    :param df: excel的数据
    :param field_index_config: 文件索引配置
    :return: 解析后的字段信息列表
    """
    if not field_index_config:
        print("field_index_config 是空的，生成失败")
        return []

    if df is None or df.iloc[:, 0].size == 0:
        print("读取到数据是空的，生成失败")
        return []

    loc_size = df.iloc[:, 0].size

    if loc_size <= 0:
        print("剪贴板未读取到数据，生成失败")
        return []

    field_list = []
    for i in range(loc_size):
        field_list.append({
            "field_name": df.loc[i][field_index_config['field_name_index']],
            "field_type": df.loc[i][field_index_config['field_type_index']],
            "field_commit": df.loc[i][field_index_config['field_mean_index']]
        })

    return field_list
