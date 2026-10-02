from enum import Enum
import re


class TokenType(Enum):
    # Define um conjunto de tokens que o analisador léxico de cobol vai reconhecer -g
    # Essa numeração permite uma regra de hierarquia de tokens? Será?
    # -g

    KEYWORD = 1, 
    # IDENTIFIER = 2,
    # NUMBER = 3,
    # BAD_TOKEN = 100 #Deveria ser o token de erro com menor prioridade


# Define quais as expressões regulares que cada token reconhece
TokenRegex = {
    TokenType.KEYWORD: r'\b(?:IF|ELSE|END|PROGRAM|DATA|DIVISION|PROCEDURE|SECTION)\b',
}

class Token:
    def __init__(self, type: TokenType, value: str):
        # Toda vez que o tokenenizador encontrar um token ele definirá qual o tipo do token e qual a  
        self.type = type
        self.value = value

class TokenizationError(Exception):
    pass