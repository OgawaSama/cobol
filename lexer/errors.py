
class TokenizationError(Exception):
    pass

class SequenceNumberAreaError(TokenizationError):
    pass

class IndicatorAreaError(TokenizationError):
    pass

class AAreaError(TokenizationError):
    pass

class BAreaError(TokenizationError):
    pass