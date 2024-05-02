"""Implementa testes para os 'steps' do analisador léxico."""

from io import StringIO

from behave import given, when, then  # pylint: disable=no-name-in-module

import errors
import lexer


@given("um programa Pascal")
def _given_pascal_program(context):
    context.program = context.text


@when("a análise léxica é executada")
def _when_lexer_executed(context):
    try:
        lex = lexer.lexer()
        lex.input(context.program)
        context.tokens = []
        token = True
        while token:
            token = lex.token()
            if token:
                context.tokens.append(token)
    except Exception as ex:  # pylint: disable=broad-except
        context.exception = ex
    else:
        context.exception = None


@then("nenhum erro ocorre")
def _then_no_error(context):
    assert context.exception is None, (
        "No exception expected but got: "
        f"{type(context.exception).__name__}({str(context.exception)})"
    )


@then("são gerados os tokens")
def _then_tokens_available(context):
    tokens = []
    with StringIO(context.text) as infile:
        for line in infile.readlines():
            value, token_type, linenum = list(
                map(str.strip, line.strip()[1:-1].split(", "))
            )
            tokens.append(
                (value[1:-1] if value[0] == '"' else value, token_type, linenum)
            )

    expected_tokens = [
        ("program", 'DIR_PROGRAM', '1'),
        ("teste", 'ID', '1'),
        (";", 'OP_EOC', '1'),
        ("var", 'DIR_VAR', '2'),
        ("a", 'ID', '3'),
        (",", 'OP_COMMA', '3'),
        ("b", 'ID', '3'),
        (":", 'OP_COLON', '3'),
        ("integer", 'TYPE_INT', '3'),
        (";", 'OP_EOC', '3'),
        ("begin", 'DIR_BEGIN', '4'),
        ("a", 'ID', '5'),
        (":=", 'OP_ATRIB', '5'),
        ("2", 'LIT_INT', '5'),
        (";", 'OP_EOC', '5'),
        ("b", 'ID', '6'),
        (":=", 'OP_ATRIB', '6'),
        ("3", 'LIT_INT', '6'),
        (";", 'OP_EOC', '6'),
        ("writeln", 'FN_WRITELN', '7'),
        ("(", 'OP_OPAR', '7'),
        ("a", 'ID', '7'),
        ("+", 'OP_SUM', '7'),
        ("b", 'ID', '7'),
        (")", 'OP_CPAR', '7'),
        (";", 'OP_EOC', '7'),
        ("end", 'DIR_END', '8'),
        (".", 'OP_PERIOD', '8'),
    ]

    assert len(tokens) == len(expected_tokens), (
        "Quantidade de tokens não é a esperada: "
        f"{len(expected_tokens)} != {len(tokens)} : {tokens}"
    )

    for i, (expected, observed) in enumerate(zip(expected_tokens, tokens)):
        assert expected == observed, f"Token número {i+1} errado: {expected} != {observed}"


@then("é gerada a exceção LexerException")
def _then_lexer_has_exception(context):
    assert context.exception is not None
    assert isinstance(context.exception, errors.LexerException)


@then('o símbolo que causou o erro é "ç"')
def _then_lexer_error_symbol(context):
    assert context.exception is not None
    assert context.exception.value == "ç"


@then("a exeção ocorreu na linha {linenum:d}")
def _then_lexer_error_line(context, linenum):
    assert context.exception is not None
    assert context.exception.line == linenum


@then("o erro ocorreu no caracter da posição {charpos:d} da linha")
def _then_lexer_error_char_pos(context, charpos):
    assert context.exception is not None
    assert context.exception.index == charpos, (
        "Posição do caracter incorreta: "
        f"{charpos} != {context.exception.index}"
    )
