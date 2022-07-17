from java.field.annonation.JacksonAnnotationGenerator import JacksonAnnotationGenerator


class FieldAnnotationManager:
    default_annotation_generators = [
        JacksonAnnotationGenerator()
    ]

    def __init__(self, config_metadata: dict):
        self.config_metadata = config_metadata
        self.opening_annotation_generators = []

        for annotation_generator in FieldAnnotationManager.default_annotation_generators:
            if annotation_generator.is_open(config_metadata):
                self.opening_annotation_generators.append(annotation_generator)

    def generate(self, field_info: dict, class_package_set: set) -> list:
        res = []
        for annotation_generator in self.opening_annotation_generators:
            annotation = annotation_generator.generate(self.config_metadata, class_package_set, field_info)
            res += annotation

        return res
