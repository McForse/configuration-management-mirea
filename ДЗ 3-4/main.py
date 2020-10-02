from MyLexer import MyLexer
from MyParser import MyParser

data = '''
(main
    (groups
        ("IKBO-01-19")
        ("IKBO-02-19")
        ("IKBO-03-19")
    )
    (students
        (age = 19, group = "IKBO-01-19", name = "Ivanov I.I.")
        (age = 18, group = "IKBO-02-19", name = "Ivanov I.I.")
        (age = 19, group = "IKBO-03-19", name = "Ivanov I.I.")
    )
    (subject = "Configuration management")
)
'''
lexer = MyLexer()

for token in lexer.tokenize(data):
    print(token)

print('\nParsing:')
parser = MyParser()
result = parser.parse(lexer.tokenize(data))
print(result)
