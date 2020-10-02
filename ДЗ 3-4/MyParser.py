from sly import Parser
from MyLexer import MyLexer
from copy import deepcopy as copy
import json


class MyParser(Parser):
    tokens = MyLexer.tokens

    @_('"(" expr_sequence ")"')
    def statement(self, p):
        return p.expr_sequence

    @_('expr "(" expr ")"')
    def expr_sequence(self, p):
        return {p.expr0: [p.expr1]}

    @_('expr "(" expr_sequence ")"')
    def expr_sequence(self, p):
        return {p.expr: [p.expr_sequence]}

    @_('expr_sequence "(" expr ")"')
    def expr_sequence(self, p):
        items_dict = p.expr_sequence
        key = list(items_dict.keys())[0]
        items_list = list(items_dict[key])
        items_list.append(p.expr)
        return {key: copy(items_list)}

    @_('expr_sequence "(" expr_sequence ")"')
    def expr_sequence(self, p):
        items_dict = p.expr_sequence0
        key = list(items_dict.keys())[0]
        items_list = list(items_dict[key])
        items_list.append(p.expr_sequence1)
        return {key: copy(items_list)}

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER

    @_('NAME')
    def expr(self, p):
        return p.NAME


if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()

    try:
        data = '''
        (var1 (var3 (var5 (var6))) (var7 (var8 (543534))) (var9))
        '''
        result = parser.parse(lexer.tokenize(data))
        print(result)
        print(json.dumps(result))
    except EOFError:
        pass

'''
Grammar (BNF)
------------------------

statement : ( expr_sequence )

expr_sequence | expr ( expr )
expr_sequence | expr ( expr_sequence )
expr_sequence | expr_sequence ( expr )
expr_sequence | expr_sequence ( expr_sequence )

expr    : NUMBER
expr    | NAME

'''
