from enum import Enum
import os

class TokenType(Enum):
    # Define um conjunto de tokens que o analisador léxico de cobol vai reconhecer -g
    # Essa numeração permite uma regra de hierarquia de tokens? Será?
    # -g

    RESERVED_KEYWORD = 1
    UNSUPPORTED_KEYWORD = 2
    NUMERIC_LITERAL = 3
    ALFANUMERIC_LITERAL = 4
    IDENTIFIER = 5
    SPECIAL_CHARACTER = 6

class Token:
    def __init__(self, type: TokenType, value: str):
        # Toda vez que o tokenenizador encontrar um token ele definirá qual o tipo do token e qual a  
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token(type={self.type}, value='{self.value}')\n"


# evil reserved keyword bit level hacking
# wtf?
# pelo amor de deus: deixar elegante depois
unsupported_keywords_file = open(os.path.expanduser("./lexer/unsupported_keywords.list"), 'r')
unsupported_keywords_list = "\\b(?:"
for line in unsupported_keywords_file:
    unsupported_keywords_list = (unsupported_keywords_list + line)[:-1] + "|"
unsupported_keywords_list = unsupported_keywords_list[:-1] + ")\\b"
unsupported_keywords_file.close()

reserved_keywords_file = open(os.path.expanduser("./lexer/reserved_keywords.list"), 'r')
reserved_keywords_list = "\\b(?:"
for line in reserved_keywords_file:
    reserved_keywords_list = (reserved_keywords_list + line)[:-1] + "|"
reserved_keywords_list = reserved_keywords_list[:-1] + ")\\b"
reserved_keywords_file.close()

# Define quais as expressões regulares que cada token reconhece
TokenRegex = {
    TokenType.RESERVED_KEYWORD: f'{reserved_keywords_list}',
    TokenType.UNSUPPORTED_KEYWORD: f'{unsupported_keywords_list}',
    TokenType.NUMERIC_LITERAL: r'[+-]?\d+(?:\.\d+)?',
    TokenType.ALFANUMERIC_LITERAL: r"""(["']).*\1""",
    TokenType.IDENTIFIER: r'[A-Z0-9](?:[A-Z0-9-]{0,28}[A-Z0-9])?',
    TokenType.SPECIAL_CHARACTER: r'[.,;()]'
}
