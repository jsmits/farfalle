"""
See https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/
"""

from abc import ABC, abstractmethod

from llama_index.core import Document
from llama_index.readers.web import (
    AsyncWebPageReader,
    SimpleWebPageReader,
    SpiderWebReader,
)


class Parser(ABC):
    @abstractmethod
    def parse(self, url: str) -> list[Document]:
        pass


class SimpleWebParser(Parser):
    def parse(self, url: str) -> list[Document]:
        return SimpleWebPageReader(html_to_text=True).load_data([url])


class AsyncWebParser(Parser):
    def parse(self, url: str) -> list[Document]:
        return AsyncWebPageReader(html_to_text=True).load_data([url])


class SpiderParser(Parser):
    def __init__(self, api_key: str):
        self.api_key = api_key  # get one at https://spider.cloud
        self.reader = SpiderWebReader(
            api_key=self.api_key,
            mode="scrape",
            # params={} # optional parameters see more on https://spider.cloud/docs/api
        )

    def parse(self, url: str) -> list[Document]:
        return self.reader.load_data(url=url)
