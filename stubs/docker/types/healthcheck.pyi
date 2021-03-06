# Stubs for docker.types.healthcheck (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import DictType
from typing import Any

class Healthcheck(DictType):
    def __init__(self, **kwargs: Any) -> None: ...
    @property
    def test(self): ...
    @test.setter
    def test(self, value: Any) -> None: ...
    @property
    def interval(self): ...
    @interval.setter
    def interval(self, value: Any) -> None: ...
    @property
    def timeout(self): ...
    @timeout.setter
    def timeout(self, value: Any) -> None: ...
    @property
    def retries(self): ...
    @retries.setter
    def retries(self, value: Any) -> None: ...
    @property
    def start_period(self): ...
    @start_period.setter
    def start_period(self, value: Any) -> None: ...
