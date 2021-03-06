# Stubs for docker.models.swarm (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .resource import Model
from typing import Any, Optional

class Swarm(Model):
    id_attribute: str = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def version(self): ...
    def get_unlock_key(self): ...
    def init(self, advertise_addr: Optional[Any] = ..., listen_addr: str = ..., force_new_cluster: bool = ..., default_addr_pool: Optional[Any] = ..., subnet_size: Optional[Any] = ..., data_path_addr: Optional[Any] = ..., **kwargs: Any): ...
    def join(self, *args: Any, **kwargs: Any): ...
    def leave(self, *args: Any, **kwargs: Any): ...
    attrs: Any = ...
    def reload(self) -> None: ...
    def unlock(self, key: Any): ...
    def update(self, rotate_worker_token: bool = ..., rotate_manager_token: bool = ..., rotate_manager_unlock_key: bool = ..., **kwargs: Any): ...
