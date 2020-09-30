from sly import Lexer


class MyLexer(Lexer):
    # Набор имен токенов
    tokens = {NUMBER, NAME, STRING, LPAREN, RPAREN}

    # Строка, содержащая игнорируемые символы (между токенами)
    ignore = ' \t'

    literals = {'='}

    # Регулярные выражения для токенов
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    LPAREN = r'\('
    RPAREN = r'\)'

    # Токен числа
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Токен комментария
    @_(r'//.*')
    def COMMENT(self, t):
        pass
