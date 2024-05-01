"""Implantação do analisador léxico."""

import ply.lex

import errors

# Lista de tokens
tokens = [
    'OP_LOGIC',
    'OP_RANGE',
    'COMMENT',
    'OP_OPAR',
    'OP_CPAR',
    'OP_OBRA',
    'OP_CBRA',
    'OP_COMMA',
    'OP_EOC',
    'OP_PERIOD',
    'OP_COLON'
]

# Tokens que são palavras reservadas
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
    'nil': 'OP_NIL'
}

tokens += reserved.values()

@ply.lex.TOKEN(r"\n+")
def t_ignore_newline(token):
    """Conto o número de linhas."""
    token.lexer.lineno += token.value.count("\n")

def lexer():
    """Cria o objeto do analisador léxico."""
    return ply.lex.lex()

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_LIT_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_LIT_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_LIT_STRING(t):
    r'\".*?\"|\'.*?\''
    t.value = t.value[1:-1]
    return t

def t_OP_ATRIB(t):
    r':='
    return t

def t_OP_SUM(t):
    r'\+|-'
    return t

def t_OP_MUL(t):
    r'\*|/|div|mod'
    return t

def t_OP_REL(t):
    r'<>|<=|>=|>|='
    return t

def t_OP_LOGIC(token):
    r'and|or|not'
    return token

def t_OP_RANGE(token):
    r'\.\.'
    return token

def t_OP_OPAR(t):
    r'\('
    return t

def t_OP_CPAR(t):
    r'\)'
    return t

def t_OP_OBRA(t):
    r'\['
    return t

def t_OP_CBRA(t):
    r'\]'
    return t

def t_OP_COMMA(t):
    r','
    return t

def t_OP_EOC(t):
    r';'
    return t

def t_OP_PERIOD(t):
    r'\.'
    return t

def t_OP_COLON(t):
    r':'
    return t

def t_COMMENT(t):
    r'\{.*?\}|\(\*.*?\*\)'
    pass

def t_error(t):
    raise Exception("Caractere não reconhecido '%s' na linha %d, posição %d" % (t.value[0], t.lineno, t.lexpos))

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'