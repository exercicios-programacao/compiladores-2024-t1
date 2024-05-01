import ply.lex as lex

# Lista de tokens
tokens = (
    'ID',
    'LIT_INT',
    'LIT_REAL',
    'LIT_STRING',
    'DIR_PROGRAM',
    'DIR_VAR',
    'DIR_PROC',
    'DIR_FUNC',
    'DIR_BEGIN',
    'DIR_END',
    'DIR_TYPE',
    'DIR_OF',
    'DIR_CONST',
    'DIR_WITH',
    'STMT_IF',
    'STMT_THEN',
    'STMT_ELSE',
    'STMT_WHILE',
    'STMT_REPEAT',
    'STMT_FOR',
    'STMT_DO',
    'STMT_UNTIL',
    'STMT_TO',
    'STMT_DOWNTO',
    'STMT_CASE',
    'TYPE_ARRAY',
    'TYPE_SET',
    'TYPE_RECORD',
    'TYPE_FILE',
    'TYPE_INT',
    'TYPE_REAL',
    'TYPE_CHAR',
    'TYPE_BOOL',
    'TYPE_STRING',
    'FN_READ',
    'FN_READLN',
    'FN_WRITE',
    'FN_WRITELN',
    'OP_NIL',
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
    'COMMENT',
)

#Tokens regulares
t_OP_ATRIB = r':='
t_OP_SUM = r'[+-]'
t_OP_MUL = r'[*\/divmod]'
t_OP_REL = r'[=<>]+|\>=|\<='
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

# Palavras reservadas e identificadores
reservedas = {
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
    '//': 'COMMENT',
}

# Expressão regular para identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservedas.get(t.value.lower(), 'ID')
    return t

# Expressões regulares para literais
def t_LIT_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_LIT_REAL(t):
    r'\d+\.\d+|\d+e[-+]?\d+'
    t.value = float(t.value)
    return t

def t_LIT_STRING(t):
    r'\".*?\"|\'.*?\''
    t.value = t.value[1:-1]  # Remove as aspas
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Rastrear o número da linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Lidar com erros léxicos
def t_error(t):
    raise Exception(f"Caractere inválido '{t.value[0]}' na linha {t.lexer.lineno}, posição {t.lexpos}")

# Criar o analisador léxico
lexer = lex.lex()

# Testar o analisador léxico
if __name__ == '__main__':
    data = '''
    program exemplo;
    var
        a, b: integer;
    begin
        a := 2;
        b := 3;
        writeln(a + b);
    end.
    '''

    lexer.input(data)
    for token in lexer:
        print(token)