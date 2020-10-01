from sly import Parser
from MyLexer import MyLexer


class MyParser(Parser):
    tokens = MyLexer.tokens

    @_('LPAREN list RPAREN')
    def statement(self, p):
        return ('statement', p.list)

    @_('expr statement')
    def expr(self, p):
        return ('item', p.statement)

    @_('LPAREN expr RPAREN')
    def statement(self, p):
        return ('statement', p.list)

    @_('expr list')
    def list(self, p):
        items_list = p.list[1]
        new_items_list = [p.expr]
        for item in items_list:
            new_items_list.append(item)
        return ('list', new_items_list)

    @_('expr expr')
    def list(self, p):
        items_list = [p.expr0, p.expr1]
        return ('list', items_list)

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER

    @_('NAME')
    def expr(self, p):
        return ('item', p.NAME)



'''
Grammar                   Action
------------------------  --------------------------------

list    : expr expr
list    | expr list

expr    : NUMBER
expr    | NAME

'''
