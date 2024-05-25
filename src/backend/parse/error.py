class ParseError(Exception):
    pass


class InvalidParser(ParseError):
    pass


class ParseConfigurationError(ParseError):
    pass
