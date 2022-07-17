from common.processor.field_info_processor.generator.IFileGenerator import IFileGenerator
from common.util import FileWriterUtil
from java.field.FieldAnnotationManager import FieldAnnotationManager


def build_all(package_name, class_name, class_package_list, field_place, config_metadata):
    print('config_metadata = {}'.format(config_metadata))
    print('field_place = {}'.format(field_place))
    print('class_package_list = {}'.format(class_package_list))

    class_package_str = '\n'.join(class_package_list)

    return f"""package {package_name};

import lombok.Data;
{class_package_str}
    
/**
 * @author {config_metadata['author']}
 * @date {config_metadata['date']}
 */
@Data
public class {class_name} {{
    {field_place}    
}}
    """


def build_field_place(class_package_set: set, field_info_list: list, config_metadata: dict):
    if not field_info_list:
        return field_info_list

    """
    field_part_place: 单个字段模板,
        commit 表示该字段的注释
        field_pre 表示字段前需要的类似注解的东西放置的地方
        field_type 表示字段类型
        field_name 表示字段名
    """

    field_part_place = """
    /**
     * {commit}
     */
    {field_pre}
    private {field_type} {field_name};
    """

    res = []
    for field_info in field_info_list:
        field_annotation_manager = FieldAnnotationManager(config_metadata)

        field_pre = field_annotation_manager.generate(field_info, class_package_set)
        combined_field_pre = '\n    '.join(field_pre)

        res.append(field_part_place.format(
            commit=field_info['field_commit'],
            field_type=field_info['field_type'],
            field_name=field_info['field_name'],
            field_pre=combined_field_pre
        ))

    str_res = ''
    for item in res:
        str_res += item

    return str_res


class JavaFileGenerator(IFileGenerator):
    def generate(self,
                 package_name: str,
                 class_name: str,
                 field_info_list: list,
                 config_metadata: dict):
        class_package_set = set()
        # 构建所有字段文本
        all_field_text = build_field_place(class_package_set, field_info_list, config_metadata)
        # 构建整个类
        all = build_all(package_name, class_name, class_package_set, all_field_text, config_metadata)
        # 写入文件
        FileWriterUtil.write(class_name + '.java', all)
