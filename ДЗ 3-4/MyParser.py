from sly import Parser
from MyLexer import MyLexer


class MyParser(Parser):
    tokens = MyLexer.tokens

    @_('expr')
    def statement(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER

    @_('NAME')
    def expr(self, p):
        return ('var', p.NAME)

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('NAME "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)

    @_('NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.STRING)

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr
