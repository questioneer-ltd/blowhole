# Stubs for docker.models.networks (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..api import APIClient
from ..utils import version_gte
from .containers import Container
from .resource import Collection, Model
from typing import Any, Optional

class Network(Model):
    @property
    def name(self): ...
    @property
    def containers(self): ...
    def connect(self, container: Any, *args: Any, **kwargs: Any): ...
    def disconnect(self, container: Any, *args: Any, **kwargs: Any): ...
    def remove(self): ...

class NetworkCollection(Collection):
    model: Any = ...
    def create(self, name: Any, *args: Any, **kwargs: Any): ...
    def get(self, network_id: Any, *args: Any, **kwargs: Any): ...
    def list(self, *args: Any, **kwargs: Any): ...
    def prune(self, filters: Optional[Any] = ...): ...
