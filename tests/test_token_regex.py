import unittest
import re
from lexer.tokens import TokenType, TokenRegex
class LexerRegexTestCase(unittest.TestCase):

    def check_match(self, token_type: TokenType, value: str, should_match: bool):
        pattern = TokenRegex[token_type]
        match = re.fullmatch(pattern, value, re.IGNORECASE)
        if should_match:
            self.assertIsNotNone(match, f"{value} should match {token_type}")
        else: 
            self.assertIsNone(match, f"{value} shouldn't match {token_type}")

    def test_reserved_keyword(self):
        valid = ["IDENTIFICATION", "DISPLAY", "PROCEDURE", "DIVISION",
                  "MOVE", "PROGRAM", "display", "dIsPlay"]
        invalid = ["ogawa_sama", "xIDENTIFICATION", "_IF",
                   "1234"]
        for val in valid:
            with self.subTest(): # faz com que não pare na primeira falha
                self.check_match(TokenType.RESERVED_KEYWORD, val, True)
        for val in invalid:
            with self.subTest(): 
                self.check_match(TokenType.RESERVED_KEYWORD, val, False)

    def test_numeric_literal(self):
        valid = ["123", "-4", "0", "67.6767", "-67", 
                 "+67", "0.0", "04", "00067"]
        invalid = ["ogawa_sama", ".5", "6,7", "+-", "++5",
                   "--8", "10."]
        for val in valid:
            with self.subTest():
                self.check_match(TokenType.NUMERIC_LITERAL, val, True)
        for val in invalid:
            with self.subTest():
                self.check_match(TokenType.NUMERIC_LITERAL, val, False)

    def test_alphanumeric_literal(self):
        valid = ['"ogawa_sama"', "'COBOL'", "''", '""', "' '",
                 '"6767"', ]
        invalid = ["ogawa_sama", '"dark souls\'', "'immergreen\""]

        for val in valid:
            with self.subTest():
                self.check_match(TokenType.ALFANUMERIC_LITERAL, val, True)
        for val in invalid:
            with self.subTest():
                self.check_match(TokenType.ALFANUMERIC_LITERAL, val, False)

    def test_identifier(self):
        valid = ["ogawa-sama", "A", "x12345", "COBOL-DA-SILVA",
                 "6767sixseven", "PROG008_STRING"]
        invalid = ["-INPUT", "INPUT-", "desgr@ca", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"]

        for val in valid:
            with self.subTest():
                self.check_match(TokenType.IDENTIFIER, val, True)
        for val in invalid:
            with self.subTest():
                self.check_match(TokenType.IDENTIFIER, val, False)

    def test_special_chatacter(self):
        valid = [".", ",", ";", "(", ")"]
        invalid = [":", "[","]", "{","}", "\""]

        for val in valid:
            with self.subTest():
                self.check_match(TokenType.SPECIAL_CHARACTER, val, True)
        for val in invalid:   
            with self.subTest():
                self.check_match(TokenType.SPECIAL_CHARACTER, val, False)

if __name__ == "__main__":
    unittest.main()