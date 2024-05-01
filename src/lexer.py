import ply.lex

import errors

palavras_reservedas= {
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
    'nil': 'OP_NIL',
    'div': 'OP_MUL',  
    'mod': 'OP_MUL', 
    'and': 'OP_LOGIC',
    'or': 'OP_LOGIC',
    'not': 'OP_LOGIC',
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
    'COMMENT',
    'OP_OPAR',
    'OP_CPAR',
    'OP_OBRA',
    'OP_CBRA',
    'OP_COMMA',
    'OP_EOC',
    'OP_PERIOD',
    'OP_COLON',
] + list(palavras_reservedas.values())

t_ignore = ' \t'
t_OP_ATRIB = r':='
t_OP_SUM = r'[+-]'
t_OP_MUL = r'[*]'
t_OP_REL = r'[=<>]=?'
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

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = palavras_reservedas.get(t.value, 'ID') 
    return t

def t_LIT_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_LIT_REAL(t):
    r'\d+\.\d+([eE][-+]?\d+)?'
    t.value = float(t.value)
    return t

def t_LIT_STRING(t):
    r'(\'[^\']*\'|\"[^\"]*\")'
    t.value = t.value[1:-1] 
    return t

def t_COMMENT(t):
    r'(\{[^\}]*\}|\(\*[\s\S]*?\*\))|\/\/.*'
    t.lexer.lineno += t.value.count('\n')  

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise errors.LexerException(t.value[0], t.lineno, t.lexpos)

lexer = ply.lex.lex()
@ply.lex.TOKEN(r"\n+")
def t_ignore_newline(token):
    """Conto o número de linhas."""
    token.lexer.lineno += token.value.count("\n")


def lexer():
    """Cria o objeto do analisador léxico."""
    return ply.lex.lex()
