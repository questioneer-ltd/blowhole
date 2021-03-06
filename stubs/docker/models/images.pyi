# Stubs for docker.models.images (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..api import APIClient
from ..constants import DEFAULT_DATA_CHUNK_SIZE
from ..errors import BuildError, ImageLoadError, InvalidArgument
from ..utils import parse_repository_tag
from ..utils.json_stream import json_stream
from .resource import Collection, Model
from typing import Any, Optional

class Image(Model):
    @property
    def labels(self): ...
    @property
    def short_id(self): ...
    @property
    def tags(self): ...
    def history(self): ...
    def save(self, chunk_size: Any = ..., named: bool = ...): ...
    def tag(self, repository: Any, tag: Optional[Any] = ..., **kwargs: Any): ...

class RegistryData(Model):
    image_name: Any = ...
    def __init__(self, image_name: Any, *args: Any, **kwargs: Any) -> None: ...
    @property
    def id(self): ...
    @property
    def short_id(self): ...
    def pull(self, platform: Optional[Any] = ...): ...
    def has_platform(self, platform: Any): ...
    attrs: Any = ...
    def reload(self) -> None: ...

class ImageCollection(Collection):
    model: Any = ...
    def build(self, **kwargs: Any): ...
    def get(self, name: Any): ...
    def get_registry_data(self, name: Any, auth_config: Optional[Any] = ...): ...
    def list(self, name: Optional[Any] = ..., all: bool = ..., filters: Optional[Any] = ...): ...
    def load(self, data: Any): ...
    def pull(self, repository: Any, tag: Optional[Any] = ..., **kwargs: Any): ...
    def push(self, repository: Any, tag: Optional[Any] = ..., **kwargs: Any): ...
    def remove(self, *args: Any, **kwargs: Any) -> None: ...
    def search(self, *args: Any, **kwargs: Any): ...
    def prune(self, filters: Optional[Any] = ...): ...
    def prune_builds(self, *args: Any, **kwargs: Any): ...

def normalize_platform(platform: Any, engine_info: Any): ...
