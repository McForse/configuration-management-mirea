import json
from MyLexer import MyLexer
from MyParser import MyParser


def toJson(data):
    lexer = MyLexer()
    parser = MyParser()

    try:
        result = parser.parse(lexer.tokenize(data))
        new_result = dict()
        for item in result['main']:
            for key, value in item.items():
                new_result[key] = value
        json_str = str(json.dumps(new_result, indent=4))
        json_str = json_str.replace('"\\\"', '"').replace('\\""', '"')
        return json_str
    except KeyError:
        return 'Main section not found!'
    except TypeError:
        return 'Syntax error!'
    except EOFError:
        return 'EOF error!'
