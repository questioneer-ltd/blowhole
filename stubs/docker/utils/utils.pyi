# Stubs for docker.utils.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

DEFAULT_HTTP_HOST: str
DEFAULT_UNIX_SOCKET: str
DEFAULT_NPIPE: str
BYTE_UNITS: Any

def create_ipam_pool(*args: Any, **kwargs: Any) -> None: ...
def create_ipam_config(*args: Any, **kwargs: Any) -> None: ...
def decode_json_header(header: Any): ...
def compare_version(v1: Any, v2: Any): ...
def version_lt(v1: Any, v2: Any): ...
def version_gte(v1: Any, v2: Any): ...
def convert_port_bindings(port_bindings: Any): ...
def convert_volume_binds(binds: Any): ...
def convert_tmpfs_mounts(tmpfs: Any): ...
def convert_service_networks(networks: Any): ...
def parse_repository_tag(repo_name: Any): ...
def parse_host(addr: Any, is_win32: bool = ..., tls: bool = ...): ...
def parse_devices(devices: Any): ...
def kwargs_from_env(ssl_version: Optional[Any] = ..., assert_hostname: Optional[Any] = ..., environment: Optional[Any] = ...): ...
def convert_filters(filters: Any): ...
def datetime_to_timestamp(dt: Any): ...
def parse_bytes(s: Any): ...
def normalize_links(links: Any): ...
def parse_env_file(env_file: Any): ...
def split_command(command: Any): ...
def format_environment(environment: Any): ...
def format_extra_hosts(extra_hosts: Any, task: bool = ...): ...
def create_host_config(self, *args: Any, **kwargs: Any) -> None: ...