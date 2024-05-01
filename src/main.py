import sys
from lexer import lexer
import errors

if __name__ == "__main__":
    try:
        
        with open(sys.argv[1], "rt") as input_file:
            lex = lexer()
            lex.input(input_file.read())

            while True:
                token = lex.token()
                if not token:
                    break
                
                print((token.value, token.type, token.lineno))

    except errors.LexerException as lexerror:
        print(f"ERROR: {str(lexerror)}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")