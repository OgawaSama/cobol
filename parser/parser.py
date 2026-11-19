from lexer.tokens import Token, TokenType
from errors import SyntaxError

class Parser:

    def __init__(self, tokens : list[Token]):
        
        self.pos = 0 # posição do token atual
        self.tokens = tokens # lista de tokens
        self.curr_token

    def current_token(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def peek(self, k=0) -> Token:
        return self.tokens[self.pos + k] if self.pos + k < len(self.tokens) else None

    def check_curr_type(self, token_type: TokenType) -> bool:
        curr_token = self.current_token()
        return curr_token is not None and curr_token.type == token_type

    def match_curr(self, token_type: TokenType) -> Token:
        if self.check_curr_type(token_type):
            self.pos += 1
            return self.current_token()

        raise SyntaxError(f"Expected token type {token_type}, but got {self.current_token().type if self.current_token() else 'None'}")

    def match_curr_optional(self, token_type) -> Token:
        if self.check_curr_type(token_type):
            self.pos += 1
            return self.current_token()
        return None

