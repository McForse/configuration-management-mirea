from sly import Parser
from MyLexer import MyLexer


class MyParser(Parser):
    tokens = MyLexer.tokens

    @_('"(" expr_sequence ")"')
    def expr_sequence(self, p):
        return p.expr_sequence

    @_('expr "(" expr ")"')
    def expr_sequence(self, p):
        return [p.expr0, [p.expr1]]

    @_('expr "(" expr_sequence ")"')
    def expr_sequence(self, p):
        return [p.expr, [p.expr_sequence]]

    @_('expr_sequence "(" expr ")"')
    def expr_sequence(self, p):
        items_list = list(p.expr_sequence)
        items_list.append([p.expr])
        return items_list

    @_('expr_sequence "(" expr_sequence ")"')
    def expr_sequence(self, p):
        items_list = list(p.expr_sequence0)
        items_list.append(p.expr_sequence1)
        return items_list

    @_('expr_sequence expr')
    def expr_sequence(self, p):
        items_list = list(p.expr_sequence)
        items_list.append(p.expr)
        return items_list

    @_('expr expr')
    def expr_sequence(self, p):
        return [p.expr0, p.expr1]

    @_('STRING')
    def expr(self, p):
        return p.STRING

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER

    @_('NAME')
    def expr(self, p):
        return p.NAME


'''
Grammar
------------------------

expr_sequence : expr expr
expr_sequence | expr ( expr )
expr_sequence | expr ( expr_sequence )
expr_sequence | ( expr_sequence )
expr_sequence | expr_sequence expr
expr_sequence | expr_sequence ( expr )
expr_sequence | expr_sequence ( expr_sequence )

expr    : NUMBER
expr    | NAME
expr    | STRING

'''
