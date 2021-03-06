# Stubs for docker.credentials.store (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .utils import create_environment_dict, find_executable
from typing import Any, Optional

class Store:
    program: Any = ...
    exe: Any = ...
    environment: Any = ...
    def __init__(self, program: Any, environment: Optional[Any] = ...) -> None: ...
    def get(self, server: Any): ...
    def store(self, server: Any, username: Any, secret: Any): ...
    def erase(self, server: Any) -> None: ...
    def list(self): ...
