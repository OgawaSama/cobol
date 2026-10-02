from tokens import TokenType, Token, TokenRegex, TokenizationError
import re

class Lexer:
    #classe 
    def __init__(self, code: str):

        self.code = code
        self.tokens = []

        self.finished_code = False

    def tokenize(self):
        # tenta tokenizar o codigo -g

        while(len(self.code) > 0):
            token = self.get_biggest_token()
            if token is None:
                #TODO processamento caso erro -g
                break
            self.tokens.append(token)
            self.code = self.code[len(token.value):] #retira o token do código, deve ter um jeito melhor de fazer isso -g

    def get_biggest_token(self):

        biggest_token = None

        # [TODO] implementar a lógica de hierarquia de tokens caso haja mais de um token possivel, acho que já é assim mas gostaria de confirmar -g

        snippet = ""
        while(len(self.code) > 0):

            snippet = self.code[:len(snippet) + 1]

            match = None
            for token_type, regex in TokenRegex.items():

                match = re.match(regex, snippet)

                if match:
                    biggest_token = Token(token_type, match.group(0))
                    break 

            if match is None and biggest_token is not None:
                return biggest_token
            else:
                raise TokenizationError(f"Tokenization error at: {snippet}")