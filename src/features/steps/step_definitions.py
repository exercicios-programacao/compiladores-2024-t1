from behave import given, when, then
from lexer import lexer

@given('o lexer recebe "{entrada}"')
def step_lexer_input(context, entrada):
    context.entrada = entrada

@when('o lexer é processado')
def step_process_lexer(context):
    lex = lexer()
    lex.input(context.entrada)
    context.tokens = []  # Lista para armazenar os tokens processados

    # Obtém os tokens do lexer
    while True:
        token = lex.token()
        if not token:
            break
        # Adiciona informações do token à lista
        context.tokens.append({
            "valor": token.value,
            "tipo": token.type,
            "linha": token.lineno,
        })

@then('deve retornar {quantidade} tokens')
def step_check_token_count(context, quantidade):
    assert len(context.tokens) >= int(quantidade), f"Esperado pelo menos {quantidade}, mas recebeu {len(context.tokens)}"

@then('o primeiro token deve ser "{valor}" com tipo "{tipo}"')
def step_check_first_token(context, valor, tipo):
    primeiro_token = context.tokens[0]
    assert str(primeiro_token["valor"]) == valor, f"Esperado {valor}, mas recebeu {str(primeiro_token['valor'])}"
    assert primeiro_token["tipo"] == tipo, f"Esperado {tipo}, mas recebeu {primeiro_token['tipo']}"

@then('o segundo token deve ser "{valor}" com tipo "{tipo}"')
def step_check_second_token(context, valor, tipo):
    segundo_token = context.tokens[1]
    assert str(segundo_token["valor"]) == valor, f"Esperado {valor}, mas recebeu {str(segundo_token['valor'])}"
    assert segundo_token["tipo"] == tipo, f"Esperado {tipo}, mas recebeu {segundo_token['tipo']}"

@then('o terceiro token deve ser "{valor}" com tipo "{tipo}"')
def step_check_third_token(context, valor, tipo):
    terceiro_token = context.tokens[2]
    assert str(terceiro_token["valor"]) == valor, f"Esperado {valor}, mas recebeu {str(terceiro_token['valor'])}"
    assert terceiro_token["tipo"] == tipo, f"Esperado {tipo}, mas recebeu {terceiro_token['tipo']}"

@then('o último token deve ser "{valor}" com tipo "{tipo}"')
def step_check_last_token(context, valor, tipo):
    ultimo_token = context.tokens[-1]  # Último token na lista
    assert ultimo_token["valor"] == valor, f"Esperado {valor}, mas recebeu {ultimo_token['valor']}"
    assert ultimo_token["tipo"] == tipo, f"Esperado {tipo}, mas recebeu {ultimo_token['tipo']}"
