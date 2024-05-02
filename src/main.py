"""Programa de teste para auxiliar no desenvolvimento."""

# Nota: Este arquivo é para uso livre, não será avaliado.

from lexer import lexer
import errors


if __name__ == "__main__":
    try:
        # pylint: disable=W1514
        with open("src/write_a_plus_b_int.pas", "rt", encoding="utf-8") as input_file:
            lex = lexer()
            lex.input(input_file.read())
            token = True  # pylint: disable=invalid-name
            while token:
                token = lex.token()
                if token:
                    print((token.value, token.type, token.lineno))
    except errors.LexerException as lexerror:
        print(f"ERROR: {str(lexerror)}")