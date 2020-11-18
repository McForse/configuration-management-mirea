# 11           0 LOAD_FAST                0 (x)  - Помещает ссылку на локальные переменные в стек.
#              2 LOAD_CONST               1 (10) - Перемещает константу 10 в стек.
#              4 BINARY_MULTIPLY                 - Двоичное умножение.
#              6 LOAD_CONST               2 (42) - Перемещает константу 42 в стек.
#              8 BINARY_ADD                      - Двоичное сложение.
#             10 RETURN_VALUE                    - Возвращает значения.

# Эквивалентное выражение на Python

import dis

def foo(x):
    return x * 10 + 42


dis.dis(foo)
