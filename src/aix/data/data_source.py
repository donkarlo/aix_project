from utilityx.data.access import Access
from utilityx.data.format.format import Format
from utilityx.data.type import type


class DataSource:
    def __init__(self, type:Type, format:Format, access:Access):
        self._type = type
        self._format = format
        self._access = access
