
def write(field_name, content):
    with open('./' + field_name, 'w', encoding='utf8') as file:
        file.write(content)
