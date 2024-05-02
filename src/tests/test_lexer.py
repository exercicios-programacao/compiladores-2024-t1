import unittest
from lexer import lexer,find_column

class TestLexer(unittest.TestCase):
    def test_id_token(self):
        lex = lexer() 
        lex.input("program var integer if then else my_id another_id_123") 
        tokens = [tok.type for tok in lex] 
        expected_tokens = ['DIR_PROGRAM', 'DIR_VAR', 'TYPE_INT', 'STMT_IF', 'STMT_THEN', 'STMT_ELSE', 'ID', 'ID']
        self.assertEqual(tokens, expected_tokens) 
        
    def test_lit_int_token(self):
        lex = lexer() 
        lex.input("42 123 987654321") 
        tokens = [(tok.type, tok.value) for tok in lex] 
        expected_tokens = [('LIT_INT', 42), ('LIT_INT', 123), ('LIT_INT', 987654321)]
        self.assertEqual(tokens, expected_tokens) 

    # def test_lit_real_token(self):
    #     lex = lexer()  
    #     lex.input("3.14 2.71828 1e10")  
    #     tokens = [(tok.type, tok.value) for tok in lex]  
    #     expected_tokens = [('LIT_REAL', 3.14), ('LIT_REAL', 2.71828), ('LIT_REAL', 1e10)]
    #     self.assertEqual(tokens, expected_tokens) 

    def test_lit_string_token(self):
        lex = lexer() 
        lex.input('"string1" \'string2\' "string with spaces"') 
        tokens = [(tok.type, tok.value) for tok in lex] 
        expected_tokens = [('LIT_STRING', 'string1'), ('LIT_STRING', 'string2'), ('LIT_STRING', 'string with spaces')]
        self.assertEqual(tokens, expected_tokens) 

    def test_comment_token(self):
        lex = lexer()
        lex.input("{comment} (* another comment *)")
        tokens = [tok.type for tok in lex if tok.type != 'COMMENT']
        expected_tokens = []
        self.assertEqual(tokens, expected_tokens)

    # def test_newline_token(self):
    #     lex = lexer()
    #     lex.input("line 1\nline 2\nline 3\n")
    #     tokens = [(tok.type, tok.value) for tok in lex] 
    #     expected_tokens = [
    #         ('ID', 'line'), ('NEWLINE', '\n'),
    #         ('ID', 'line'), ('NEWLINE', '\n'),
    #         ('ID', 'line'), ('NEWLINE', '\n')
    #         ]
    #     self.assertEqual(tokens, expected_tokens)
    #     self.assertEqual(lex.lineno, 4) 

class TestIgnoreNewline(unittest.TestCase):
    def test_ignore_newline(self):
        lex = lexer()  
        lex.input("linha 1\nlinha 2\nlinha 3\n")  
        lex.lineno = 1 
        for _ in lex:
            pass
        self.assertEqual(lex.lineno, 4) 

if __name__ == '__main__':
    unittest.main()