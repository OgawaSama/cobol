from enum import Enum
import re


class TokenType(Enum):
    # Define um conjunto de tokens que o analisador léxico de cobol vai reconhecer -g
    # Essa numeração permite uma regra de hierarquia de tokens? Será?
    # -g

    RESERVED_KEYWORD = 1,
    NUMERIC_LITERAL = 2,
    ALFANUMERIC_LITERAL = 3,
    IDENTIFIER = 4,
    SPECIAL_CHARACTER = 5

# Define quais as expressões regulares que cada token reconhece
TokenRegex = {
    TokenType.RESERVED_KEYWORD: r'\b(?:IDENTIFICATION|ENVIRONMENT|DATA|PROCEDURE|DIVISION|SECTION|DISPLAY|ACCEPT|PERFORM|STOP|RUN|IF|ELSE|MOVE)\b',
    TokenType.NUMERIC_LITERAL: r'[+-]?\d+\.\d+',
    TokenType.ALFANUMERIC_LITERAL: r"""(['"]).*\1""",
    TokenType.IDENTIFIER: r'[A-Z0-9](?:[A-Z0-9-]{0,28}[A-Z0-9])?',
    TokenType.SPECIAL_CHARACTER: r'[.,;()]'
}

class Token:
    def __init__(self, type: TokenType, value: str):
        # Toda vez que o tokenenizador encontrar um token ele definirá qual o tipo do token e qual a  
        self.type = type
        self.value = value

