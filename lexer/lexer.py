
from .tokens import TokenType, Token, TokenRegex
from .errors import SequenceNumberAreaError, IndicatorAreaError, AAreaError, BAreaError, TokenizationError, UnsupportedKeyword, ProgramAreaError
import re



def lexer(code: str) -> list[Token]:
    #Função principal do analisador léxico (antes era uma classe, mas não parecia necessário guardar estados e transformei em função) -g

    tokens = []

    buffer = "" # buffer do literal incompleto 
    incomplete_literal = False

    line_count = 0

    for line in code.splitlines():
        line_count = line_count + 1
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
                #else:
                #   raise IndicatorAreaError(f"Linha {line_count} \"[{line}]\": Indicador de continuacao de literal invalido.")
            case 'D':
                # [TODO] implementar a lógica de debug -g
                pass
            case _:
                raise IndicatorAreaError(f"Linha {line_count} \"[{line}]\": Indicador de indicador inválido: {indicator_area}")

        program_area = line[7:72]
        if program_area == '':
            continue

        try:
            if incomplete_literal:
                program_area = buffer + program_area[1:]
                buffer = ""
                incomplete_literal = False
            # pro caso do literal que continua na prox linha -o
            incomplete_literal_pattern = re.compile("""^["'][^"']*$""") #inicia com aspas e nao fecha elas
            if (incomplete_literal_pattern.match(program_area)):
                incomplete_literal = True
                buffer = buffer + program_area
                continue
            
            numeric_pattern = re.compile("""["']\d+["']""")
            if (numeric_pattern.match(program_area)):  #quando for numerico mas que durou varias linhas, eh lido como alfanumerico. transformar de volta para numerico. -o
              program_area = program_area[1:-1]
            
            tokenize(program_area, tokens)
            
        except TokenizationError as e:
            raise ProgramAreaError(f"Linha {line_count} \"[{line}]\": Erro na área de programa: {e}")
            
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
