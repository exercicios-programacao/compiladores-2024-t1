Feature: Lexer Testing
  Scenario: Testar identificadores
    Given o lexer recebe "var x = 10"
    When o lexer é processado
    Then deve retornar 3 tokens
    And o primeiro token deve ser "var" com tipo "DIR_VAR"
    And o segundo token deve ser "x" com tipo "ID"
    And o terceiro token deve ser "=" com tipo "OP_REL"

  Scenario: Testar literais
    Given o lexer recebe "123 + 3.14"
    When o lexer é processado
    Then deve retornar 3 tokens
    And o primeiro token deve ser "123" com tipo "LIT_INT"
    And o segundo token deve ser "+" com tipo "OP_SUM"
    And o terceiro token deve ser "3.14" com tipo "LIT_REAL"
