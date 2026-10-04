from enum import Enum
import os

class TokenType(Enum):
    # Define um conjunto de tokens que o analisador léxico de cobol vai reconhecer -g
    # Essa numeração permite uma regra de hierarquia de tokens? Será?
    # -g

    RESERVED_KEYWORD = 1,
    UNSUPPORTED_KEYWORD = 2
    NUMERIC_LITERAL = 3,
    ALFANUMERIC_LITERAL = 4,
    IDENTIFIER = 5,
    SPECIAL_CHARACTER = 6

class Token:
    def __init__(self, type: TokenType, value: str):
        # Toda vez que o tokenenizador encontrar um token ele definirá qual o tipo do token e qual a  
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token(type={self.type}, value='{self.value}')"


# evil reserved keyword bit level hacking
# wtf?
file = open(os.path.expanduser("./lexer/unsupported_keywords.list"), 'r')
list = "\\b(?:"
for line in file:
    list = (list + line)[:-1] + "|"
list = list[:-1] + ")\\b"
file.close()

# Define quais as expressões regulares que cada token reconhece
TokenRegex = {
    TokenType.RESERVED_KEYWORD: r'\b(?:IDENTIFICATION|ENVIRONMENT|DATA|PROCEDURE|DIVISION|SECTION|DISPLAY|ACCEPT|PERFORM|STOP|RUN|IF|ELSE|MOVE)\b',
    TokenType.UNSUPPORTED_KEYWORD: f'{list}',
    TokenType.NUMERIC_LITERAL: r'[+-]?\d+\.\d+',
    TokenType.ALFANUMERIC_LITERAL: r"""(['"]).*\1""",
    TokenType.IDENTIFIER: r'[A-Z0-9](?:[A-Z0-9-]{0,28}[A-Z0-9])?',
    TokenType.SPECIAL_CHARACTER: r'[.,;()]'
}
