# Stubs for docker.api.network (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..errors import InvalidVersion
from ..utils import check_resource, minimum_version, version_lt
from typing import Any, Optional

class NetworkApiMixin:
    def networks(self, names: Optional[Any] = ..., ids: Optional[Any] = ..., filters: Optional[Any] = ...): ...
    def create_network(self, name: Any, driver: Optional[Any] = ..., options: Optional[Any] = ..., ipam: Optional[Any] = ..., check_duplicate: Optional[Any] = ..., internal: bool = ..., labels: Optional[Any] = ..., enable_ipv6: bool = ..., attachable: Optional[Any] = ..., scope: Optional[Any] = ..., ingress: Optional[Any] = ...): ...
    def prune_networks(self, filters: Optional[Any] = ...): ...
    def remove_network(self, net_id: Any) -> None: ...
    def inspect_network(self, net_id: Any, verbose: Optional[Any] = ..., scope: Optional[Any] = ...): ...
    def connect_container_to_network(self, container: Any, net_id: Any, ipv4_address: Optional[Any] = ..., ipv6_address: Optional[Any] = ..., aliases: Optional[Any] = ..., links: Optional[Any] = ..., link_local_ips: Optional[Any] = ...) -> None: ...
    def disconnect_container_from_network(self, container: Any, net_id: Any, force: bool = ...) -> None: ...