from sly import Parser
from MyLexer import MyLexer


class MyParser(Parser):
    tokens = MyLexer.tokens

    @_('expr')
    def program(self, p):
        return p.expr

    @_('"(" expr_list ")"')
    def expr(self, p):
        return p.expr_list

    @_('data')
    def expr(self, p):
        return p.data

    @_('expr expr_list')
    def expr_list(self, p):
        return [p.expr] + p.expr_list

    @_('expr expr')
    def expr_list(self, p):
        return [p.expr0, p.expr1]

    @_('var_assign')
    def data(self, p):
        return p.var_assign[0], p.var_assign[1]

    @_('var')
    def data(self, p):
        return p.var

    @_('var "=" STRING')
    def var_assign(self, p):
        return p.var, p.STRING

    @_('var "=" NUMBER')
    def var_assign(self, p):
        return p.var, p.NUMBER

    @_('STRING')
    def var(self, p):
        return p.STRING

    @_('NUMBER')
    def var(self, p):
        return p.NUMBER

    @_('NAME')
    def var(self, p):
        return p.NAME


'''
Grammar (BNF)
------------------------

program    : expr

expr       : ( expr_list )
expr       | data

expr_list  | expr expr_list
expr_list  : expr expr

data       : var_assign
data       | var

var_assign : var = STRING
var_assign | var = NUMBER

var        : STRING
var        | NUMBER
var        | NAME

'''
