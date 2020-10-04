import json
from MyLexer import MyLexer
from MyParser import MyParser


def normalize(data):
    new_data = dict()

    for i in range(len(data)):
        if type(data[i]) is str and i + 1 < len(data) and type(data[i + 1]) is list:
            new_data[data[i]] = normalize_list(data[i + 1])
            i += 1
        elif type(data[i]) is tuple:
            new_data[data[i][0]] = data[i][1]

    return new_data


def normalize_list(data):
    new_data = list()

    if list_of_tuple(data):
        new_list = dict()

        for item in data:
            new_list[item[0]] = item[1]

        return new_list

    for item in data:
        itype = type(item)

        if itype is str or itype is int:
            new_data.append(item)
        if itype is list:
            new_data.append(normalize_list(item))

    return new_data


def list_of_tuple(items_list):
    for item in items_list:
        if type(item) is not tuple:
            return False
    return True


def toJson(data):
    lexer = MyLexer()
    parser = MyParser()

    try:
        result = parser.parse(lexer.tokenize(data))
        print(result)
        new_result = normalize(result)
        json_str = json.dumps(new_result, indent=4, ensure_ascii=False,)
        json_str = json_str.replace('"\\\"', '"').replace('\\""', '"')
        return json_str
    except TypeError:
        return 'Syntax error!'
    except EOFError:
        return 'EOF error!'
