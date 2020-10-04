import json
from MyLexer import MyLexer
from MyParser import MyParser
import re


class Method:
    def __init__(self, properties, output):
        self.properties = properties
        self.output = output


methods_dict = dict()


def add_method(data):
    methods_dict[data[0]] = Method(data[1], data[2])


def normalize(data):
    new_data = dict()

    for i in range(len(data)):
        item = data[i]

        if type(item) is str and i + 1 < len(data) and type(data[i + 1]) is list:
            if item == '_def':
                add_method(data[i + 1])
            else:
                new_data[item] = normalize_list(data[i + 1])
        elif type(item) is tuple:
            new_data[item[0]] = item[1]

    return new_data


def normalize_list(data):
    new_data = list()

    if list_of_tuple(data):
        return create_dict(data)

    i = int()
    while i < len(data):
        item = data[i]
        itype = type(item)

        if type(item) is str and i + 1 < len(data) and type(data[i + 1]) is list:
            if item == '_generate_text':
                new_data += generate(data[i + 1])
            elif item in methods_dict.keys():
                properties = methods_dict[item].properties
                output = methods_dict[item].output
                config_data = data[i + 1]
                if len(properties) != len(config_data):
                    raise TypeError
                new_item = dict()
                for j in range(len(properties)):
                    new_item[properties[j]] = config_data[j]
                new_output = dict()
                for item in output:
                    key = re.findall(r'\${.*}', item)
                    if len(key) != 0:
                        key = str(key[0][2:-1])
                        new_output[key] = re.sub(r'\${.*}', str(new_item[key]), item)
                    else:
                        new_output[item] = new_item[item]
                new_data.append(new_output)
            else:
                new_data.append({item: normalize_list(data[i + 1])})
            i += 1
        elif itype is str or itype is int:
            new_data.append(item)
        elif itype is list:
            new_data.append(normalize_list(item))
        elif type(data[i]) is tuple:
            new_data[data[i][0]] = data[i][1]
        i += 1

    return new_data


def create_dict(data):
    new_dict = dict()
    for item in data:
        new_dict[item[0]] = item[1]
    return new_dict


def list_of_tuple(items_list):
    for item in items_list:
        if type(item) is not tuple:
            return False
    return True


def generate(data):
    generated_list = list()

    if len(data) != 3:
        raise TypeError
    for i in range(data[1], data[2] + 1):
        generated_list.append(re.sub(r'\*', str(i), data[0]))
    return generated_list


def toJson(data):
    lexer = MyLexer()
    parser = MyParser()

    try:
        result = parser.parse(lexer.tokenize(data))
        new_result = normalize(result)
        json_str = json.dumps(new_result, indent=4, ensure_ascii=False)
        json_str = json_str.replace('"\\\"', '"').replace('\\""', '"')
        return json_str
    except TypeError:
        return 'Syntax error!'
    except EOFError:
        return 'EOF error!'
