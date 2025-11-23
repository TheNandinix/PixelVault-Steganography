# Syllabus Unit 3: Character to Number Conversion & Base Conversion
def data_to_binary(data):
    if isinstance(data, str):
        return [format(ord(i), '08b') for i in data]
    return []