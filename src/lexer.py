"""Implantação do analisador léxico."""

import ply.lex as lex

import errors

# Palavras reservadas
reserved = {
    'program': 'DIR_PROGRAM',
    'var': 'DIR_VAR',
    'procedure': 'DIR_PROC',
    'function': 'DIR_FUNC',
    'begin': 'DIR_BEGIN',
    'end': 'DIR_END',
    'type': 'DIR_TYPE',
    'of': 'DIR_OF',
    'const': 'DIR_CONST',
    'with': 'DIR_WITH',
    'if': 'STMT_IF',
    'then': 'STMT_THEN',
    'else': 'STMT_ELSE',
    'while': 'STMT_WHILE',
    'repeat': 'STMT_REPEAT',
    'for': 'STMT_FOR',
    'do': 'STMT_DO',
    'until': 'STMT_UNTIL',
    'to': 'STMT_TO',
    'downto': 'STMT_DOWNTO',
    'case': 'STMT_CASE',
    'array': 'TYPE_ARRAY',
    'set': 'TYPE_SET',
    'record': 'TYPE_RECORD',
    'file': 'TYPE_FILE',
    'integer': 'TYPE_INT',
    'real': 'TYPE_REAL',
    'character': 'TYPE_CHAR',
    'boolean': 'TYPE_BOOL',
    'string': 'TYPE_STRING',
    'read': 'FN_READ',
    'readln': 'FN_READLN',
    'write': 'FN_WRITE',
    'writeln': 'FN_WRITELN',
}

tokens = [
    'ID',
    'LIT_INT',
    'LIT_REAL',
    'LIT_STRING',
    'OP_ATRIB',
    'OP_SUM',
    'OP_MUL',
    'OP_REL',
    'OP_LOGIC',
    'OP_RANGE',
    'OP_OPAR',
    'OP_CPAR',
    'OP_OBRA',
    'OP_CBRA',
    'OP_COMMA',
    'OP_EOC',
    'OP_PERIOD',
    'OP_COLON',
    'COMMENT'
] + list(reserved.values())

# Expressões regulares para tokens
t_OP_ATRIB = r':='
t_OP_SUM = r'[+]'
t_OP_MUL = r'[*]'
t_OP_REL = r'[=<>]+|>=|<=|<>'
t_OP_LOGIC = r'and|or|not'
t_OP_RANGE = r'\.\.'
t_OP_OPAR = r'\('
t_OP_CPAR = r'\)'
t_OP_OBRA = r'\['
t_OP_CBRA = r'\]'
t_OP_COMMA = r','
t_OP_EOC = r';'
t_OP_PERIOD = r'\.'
t_OP_COLON = r':'
t_COMMENT = r'(\{[\s\S]*?\})|(\(\*[\s\S]*?\*\))|\/\/.*'

# Caracteres ignorados
t_ignore = ' \t'

# Função para contar novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Identificadores e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Literal inteiro
def t_LIT_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Literal real
def t_LIT_REAL(t):
    r'\d+\.\d+([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

# Literal string
def t_LIT_STRING(t):
    r'(\'[^\']*\'|\"[^\"]*\")'
    t.value = t.value[1:-1]  # Remove as aspas
    return t

# Tratamento de erro
def t_error(t):
    raise Exception(f"Caractere inválido '{t.value[0]}' na linha {t.lineno}, posição {t.lexpos - t.lexer.lexdata.rfind('\\n', 0, t.lexpos)}.")

# Construir o lexer
lexer = lex.lex()

# Testar o lexer
if __name__ == "__main__":
    data = """
    program Test;
    var
        x: integer;
    begin
        x := 10;
    end.
    """
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # Sem mais entradas
        print(tok)
