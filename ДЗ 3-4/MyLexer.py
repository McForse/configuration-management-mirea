from sly import Lexer


class MyLexer(Lexer):
    # Набор имен токенов
    tokens = {NUMBER, NAME, STRING}

    # Строка, содержащая игнорируемые символы (между токенами)
    ignore = ' \t'

    # Токен комметария
    ignore_comment = r'\#.*'

    literals = {'(', ')', '='}

    # Регулярные выражения для токенов
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    def __init__(self):
        self.nesting_level = 0

    # Токен числа
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Отслеживание номера строки
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print('\033[91m' + 'Line %d: Bad character %r' % (self.lineno, t.value[0]) + '\033[0m')
        self.index += 1


if __name__ == '__main__':
    data = '''
(var1 var2)
'''
    lexer = MyLexer()
    for token in lexer.tokenize(data):
        print(token)
