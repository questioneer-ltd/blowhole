# Stubs for docker.transport.unixconn (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import requests.packages.urllib3 as urllib3
from docker.transport.basehttpadapter import BaseHTTPAdapter
from six.moves import http_client as httplib
from typing import Any, Optional

RecentlyUsedContainer: Any

class UnixHTTPResponse(httplib.HTTPResponse):
    def __init__(self, sock: Any, *args: Any, **kwargs: Any) -> None: ...

class UnixHTTPConnection(httplib.HTTPConnection):
    base_url: Any = ...
    unix_socket: Any = ...
    timeout: Any = ...
    disable_buffering: bool = ...
    def __init__(self, base_url: Any, unix_socket: Any, timeout: int = ...) -> None: ...
    sock: Any = ...
    def connect(self) -> None: ...
    def putheader(self, header: Any, *values: Any) -> None: ...
    def response_class(self, sock: Any, *args: Any, **kwargs: Any): ...

class UnixHTTPConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    base_url: Any = ...
    socket_path: Any = ...
    timeout: Any = ...
    def __init__(self, base_url: Any, socket_path: Any, timeout: int = ..., maxsize: int = ...) -> None: ...

class UnixHTTPAdapter(BaseHTTPAdapter):
    __attrs__: Any = ...
    socket_path: Any = ...
    timeout: Any = ...
    pools: Any = ...
    def __init__(self, socket_url: Any, timeout: int = ..., pool_connections: Any = ...) -> None: ...
    def get_connection(self, url: Any, proxies: Optional[Any] = ...): ...
    def request_url(self, request: Any, proxies: Any): ...
