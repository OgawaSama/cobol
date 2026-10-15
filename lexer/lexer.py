
from .tokens import TokenType, Token, TokenRegex
from .errors import SequenceNumberAreaError, IndicatorAreaError, AAreaError, BAreaError, TokenizationError, UnsupportedKeyword
import re



def lexer(code: str) -> list[Token]:
    #Função principal do analisador léxico (antes era uma classe, mas não parecia necessário guardar estados e transformei em função) -g

    tokens = []

    buffer = "" # buffer do literal incompleto 
    incomplete_literal = False

    for line in code.splitlines():
        sequence_number_area = line[:6] # Ignorei mesmo #toleve #vivendonoperigo #cubol -g
        indicator_area = line[6:7] # [TODO] De fato checar se há uma continuação de literal ou outras coisas
        
        a_area = line[7:11]
        b_area = line[11:72]

        match indicator_area:
            case ' ':
                pass # ignora linha em branco
            case '':
                pass # ignora linha em branco
            case '*':
                continue # ignora linha de comentário
            case '/':
                continue # ignora linha de comentário
            case '-':
                if (incomplete_literal == True):    # se a linha anterior marcou como incompleto, continuar. cc, erro.
                    pass
                else:
                    raise IndicatorAreaError(f"Linha [{line}]: Indicador de continuacao de literal invalido.")
            case 'D':
                # [TODO] implementar a lógica de debug -g
                pass
            case _:
                raise IndicatorAreaError(f"Linha [{line}]: Indicador de indicador inválido: {indicator_area}")

        if a_area == '':
            continue # linha em branco
        try:
            tokenize(a_area, tokens)
        except TokenizationError as e:
            raise AAreaError(f"Linha [{line}]: Erro na área A: {e}")

        if b_area == '':
            continue # linha em branco
        try:
            if (incomplete_literal == True): 
                b_area = buffer + b_area[1:]
                buffer = ""
                incomplete_literal = False
            # pro caso do literal que continua na prox linha -o
            incomplete_literal_pattern = re.compile("""^["'][^"']*$""") #inicia com aspas e nao fecha elas
            if (incomplete_literal_pattern.match(b_area)):
                incomplete_literal = True
                buffer = buffer + b_area
                continue
            numeric_pattern = re.compile("""["']\d+["']""")
            if (numeric_pattern.match(b_area)):  #quando for numerico mas que durou varias linhas, eh lido como alfanumerico. transformar de volta para numerico. -o
                b_area = b_area[1:-1]

            tokenize(b_area, tokens)
        except TokenizationError as e:
            raise BAreaError(f"Linha [{line}]: Erro na área B: {e}")

        # print(tokens)
    return tokens


def tokenize(code: str, tokens: list[Token]) -> None:

    while len(code) > 0:

        if code[0].isspace():
            code = code[1:]
            continue

        token = get_biggest_token(code)

        tokens.append(token)
        code = code[len(token.value):]


def get_biggest_token(code) -> Token:

    biggest_token = None
    
    snippet = ""


    while len(snippet) < len(code):

        snippet = code[:len(snippet) + 1]

        match = None

        for token_type, regex in TokenRegex.items():

            match = re.fullmatch(regex, snippet, re.IGNORECASE)

            if match:
                biggest_token = Token(token_type, match.group(0).upper())
                break

        # if match is None:
        #     if biggest_token is not None:
        #         return biggest_token

        #     raise TokenizationError(
        #         f"Tokenization error at: {snippet}"
        #     )

    if biggest_token is not None:
        return biggest_token

    raise TokenizationError(
        f"Tokenization error at: {code}"
    )
