"""Implantação do analisador léxico."""

import ply.lex
from errors import LexerException


@ply.lex.TOKEN(r"\n+")
def t_ignore_newline(token):
    """Conto o número de linhas."""
    token.lexer.lineno += token.value.count("\n")


def lexer():
    """Cria o objeto do analisador léxico."""

    reservadas = {
        'program' : 'DIR_PROGRAM',
        'var' : 'DIR_VAR',
        'procedure' : 'DIR_PROC',
        'function' : 'DIR_FUNC',
        'begin' : 'DIR_BEGIN',
        'end' : 'DIR_END',
        'type' : 'DIR_TYPE',
        'of' : 'DIR_OF',
        'const' : 'DIR_CONST',
        'with' : 'DIR_WITH',
        'if' : 'STMT_IF',
        'then' : 'STMT_THEN',
        'else' : 'STMT_ELSE',
        'while' : 'STMT_WHILE',
        'repeat' : 'STMT_REPEAT',
        'for' : 'STMT_FOR',
        'do' : 'STMT_DO',
        'until' : 'STMT_UNTIL',
        'to' : 'STMT_TO',
       ' downto' : 'STMT_DOWNTO',
        'case' : 'STMT_CASE',
        'array' : 'TYPE_ARRAY',
        'set' : 'TYPE_SET',
        'record' : 'TYPE_RECORD',
        'file' : 'TYPE_FILE',
        'integer' : 'TYPE_INT',
        'real' : 'TYPE_REAL',
        'character' : 'TYPE_CHAR',
        'boolean' : 'TYPE_BOOL',
        'string' : 'TYPE_STRING',
    } 

    tokens = [
        'ID',
        'LIT_INT',
        'LIT_REAL',
        'LIT_STRING',
        'FN_READ',
        'FN_READLN',
        'FN_WHITE',
        'FN_WHITELN',
        'OP_NIL',
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
    ] + list((reservadas.values()))

    
    t_OP_ATRIB = r':='
    t_OP_SUM = r'[-+]'
    t_OP_RANGE = r'\..' 
    t_OP_MUL = r'\*'
    t_OP_OPAR = r'\('
    t_OP_CPAR = r'\)'
    t_OP_OBRA = r'\['
    t_OP_CBRA = r'\]'
    t_OP_COMMA = r'\,'
    t_OP_EOC = r'\;'
    t_OP_PERIOD = r'\.'
    t_OP_COLON = r'\:'
    t_ignore = ' \t\x0c'


    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reservadas.get(t.value,'ID')
        return t
    

    def t_LIT_INT(t):
        r'\d+'
        t.value = int(t.value)
        return t
    

    def t_LIT_REAL(t):
        r'\d+(\.\d+)?(e[-+]?\d+)?'
        return t
    

    def t_LIT_STRING(t):
        r'\'[a-zA-Z_][a-zA-Z_0-9]*\'|\"[a-zA-Z_][a-zA-Z_0-9]*\"'
        return t


    def t_OP_NIL(t):
        r'nil'
        return t


    def t_OP_REL(t):
        r'=|<>|<=|>=|>|<'
        return t
    

    def t_OP_LOGIC(t):
        r'and|or|not'
        return t
    

    def t_COMMENT(t):
        r'//.*|\{.*\}|\(\*.*\*\)'
        pass


    def t_FN_READ(t):
        r'read'
        return t


    def t_FN_READLN(t):
        r'readln'
        return t


    def t_FN_WRITE(t):
        r'write'
        return t


    def t_FN_WRITELN(t):
        r'writeln'
        return t
    

    def find_column(input, token):
        line_start = input.rfind('\n', 0, token) + 1
        return (token - line_start) 


    def t_error(t):
        raise LexerException(t.value[0], t.lexer.lineno, find_column(t.lexer.lexdata, t.lexpos))

               
    return ply.lex.lex()
