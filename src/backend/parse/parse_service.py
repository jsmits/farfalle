import os

from dotenv import load_dotenv
from llama_index.core import Document

from .error import InvalidParser, ParseConfigurationError
from .parsers import AsyncWebParser, Parser, SimpleWebParser, SpiderParser

load_dotenv()


def get_spider_api_key() -> str:
    try:
        return os.environ["SPIDER_API_KEY"]
    except KeyError:
        raise ParseConfigurationError(
            "Spider API key is not set in the environment variables. Please set the SPIDER_API_KEY "
            "environment variable or set HTML_PARSER to 'simpleweb' or 'asyncweb'.",
        )


def get_parser() -> Parser:
    parser = os.getenv("HTML_PARSER")

    if parser == "simpleweb":
        return SimpleWebParser()

    elif parser == "asyncweb":
        return AsyncWebParser()

    elif parser == "spider":
        api_key = get_spider_api_key()
        return SpiderParser(api_key)

    else:
        raise InvalidParser(
            "Invalid parser. Please set the HTML_PARSER environment variable to either "
            "'simpleweb', 'asyncweb' or 'spider'."
        )


async def parse_url(url: str) -> list[Document]:
    parser = get_parser()
    return parser.parse(url)
