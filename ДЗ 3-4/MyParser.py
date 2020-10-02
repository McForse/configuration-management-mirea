from sly import Parser
from MyLexer import MyLexer
from copy import deepcopy as copy


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

    @_('expr_list "," var_assign')
    def expr_list(self, p):
        items_dict = p.expr_list
        items_dict[p.var_assign[0]] = p.var_assign[1]
        return items_dict

    @_('var_assign "," var_assign')
    def expr_list(self, p):
        items_dict = {p.var_assign0[0]: p.var_assign0[1], p.var_assign1[0]: p.var_assign1[1]}
        return items_dict

    @_('expr_list')
    def expr(self, p):
        return p.expr_list

    @_('var_assign')
    def expr(self, p):
        items_dict = {p.var_assign[0]: p.var_assign[1]}
        return items_dict

    @_('var')
    def expr(self, p):
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

statement     : ( expr_sequence )

expr_sequence | expr ( expr )
expr_sequence | expr ( expr_sequence )
expr_sequence | expr_sequence ( expr )
expr_sequence | expr_sequence ( expr_sequence )

expr_list     : expr, var_assign
expr_list     | var_assign, var_assign

expr          : expr_list
expr          | var_assign
expr          | var

var_assign    : var = STRING
var_assign    | var = NUMBER

var           : STRING
var           | NUMBER
var           | NAME

'''
