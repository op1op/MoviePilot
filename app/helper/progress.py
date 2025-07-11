from enum import Enum
from typing import Union, Optional

from app.schemas.types import ProgressKey
from app.utils.singleton import WeakSingleton


class ProgressHelper(metaclass=WeakSingleton):

    def __init__(self):
        self._process_detail = {}

    def init_config(self):
        pass

    def __reset(self, key: Union[ProgressKey, str]):
        if isinstance(key, Enum):
            key = key.value
        self._process_detail[key] = {
            "enable": False,
            "value": 0,
            "text": "请稍候..."
        }

    def start(self, key: Union[ProgressKey, str]):
        self.__reset(key)
        if isinstance(key, Enum):
            key = key.value
        self._process_detail[key]['enable'] = True

    def end(self, key: Union[ProgressKey, str]):
        if isinstance(key, Enum):
            key = key.value
        if not self._process_detail.get(key):
            return
        self._process_detail[key] = {
            "enable": False,
            "value": 100,
            "text": "正在处理..."
        }

    def update(self, key: Union[ProgressKey, str], value: Union[float, int] = None, text: Optional[str] = None):
        if isinstance(key, Enum):
            key = key.value
        if not self._process_detail.get(key, {}).get('enable'):
            return
        if value:
            self._process_detail[key]['value'] = value
        if text:
            self._process_detail[key]['text'] = text

    def get(self, key: Union[ProgressKey, str]) -> dict:
        if isinstance(key, Enum):
            key = key.value
        return self._process_detail.get(key)
