# Stubs for docker.types.services (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..constants import IS_WINDOWS_PLATFORM
from ..utils import check_resource, convert_service_networks, format_environment, format_extra_hosts, parse_bytes, split_command
from typing import Any, Optional

class TaskTemplate(dict):
    def __init__(self, container_spec: Any, resources: Optional[Any] = ..., restart_policy: Optional[Any] = ..., placement: Optional[Any] = ..., log_driver: Optional[Any] = ..., networks: Optional[Any] = ..., force_update: Optional[Any] = ...) -> None: ...
    @property
    def container_spec(self): ...
    @property
    def resources(self): ...
    @property
    def restart_policy(self): ...
    @property
    def placement(self): ...

class ContainerSpec(dict):
    def __init__(self, image: Any, command: Optional[Any] = ..., args: Optional[Any] = ..., hostname: Optional[Any] = ..., env: Optional[Any] = ..., workdir: Optional[Any] = ..., user: Optional[Any] = ..., labels: Optional[Any] = ..., mounts: Optional[Any] = ..., stop_grace_period: Optional[Any] = ..., secrets: Optional[Any] = ..., tty: Optional[Any] = ..., groups: Optional[Any] = ..., open_stdin: Optional[Any] = ..., read_only: Optional[Any] = ..., stop_signal: Optional[Any] = ..., healthcheck: Optional[Any] = ..., hosts: Optional[Any] = ..., dns_config: Optional[Any] = ..., configs: Optional[Any] = ..., privileges: Optional[Any] = ..., isolation: Optional[Any] = ..., init: Optional[Any] = ...) -> None: ...

class Mount(dict):
    def __init__(self, target: Any, source: Any, type: str = ..., read_only: bool = ..., consistency: Optional[Any] = ..., propagation: Optional[Any] = ..., no_copy: bool = ..., labels: Optional[Any] = ..., driver_config: Optional[Any] = ..., tmpfs_size: Optional[Any] = ..., tmpfs_mode: Optional[Any] = ...) -> None: ...
    @classmethod
    def parse_mount_string(cls, string: Any): ...

class Resources(dict):
    def __init__(self, cpu_limit: Optional[Any] = ..., mem_limit: Optional[Any] = ..., cpu_reservation: Optional[Any] = ..., mem_reservation: Optional[Any] = ..., generic_resources: Optional[Any] = ...) -> None: ...

class UpdateConfig(dict):
    def __init__(self, parallelism: int = ..., delay: Optional[Any] = ..., failure_action: str = ..., monitor: Optional[Any] = ..., max_failure_ratio: Optional[Any] = ..., order: Optional[Any] = ...) -> None: ...

class RollbackConfig(UpdateConfig): ...

class RestartConditionTypesEnum:
    NONE: Any = ...
    ON_FAILURE: Any = ...
    ANY: Any = ...

class RestartPolicy(dict):
    condition_types: Any = ...
    def __init__(self, condition: Any = ..., delay: int = ..., max_attempts: int = ..., window: int = ...) -> None: ...

class DriverConfig(dict):
    def __init__(self, name: Any, options: Optional[Any] = ...) -> None: ...

class EndpointSpec(dict):
    def __init__(self, mode: Optional[Any] = ..., ports: Optional[Any] = ...) -> None: ...

def convert_service_ports(ports: Any): ...

class ServiceMode(dict):
    def __init__(self, mode: Any, replicas: Optional[Any] = ...) -> None: ...
    @property
    def mode(self): ...
    @property
    def replicas(self): ...

class SecretReference(dict):
    def __init__(self, secret_id: Any, secret_name: Any, filename: Optional[Any] = ..., uid: Optional[Any] = ..., gid: Optional[Any] = ..., mode: int = ...) -> None: ...

class ConfigReference(dict):
    def __init__(self, config_id: Any, config_name: Any, filename: Optional[Any] = ..., uid: Optional[Any] = ..., gid: Optional[Any] = ..., mode: int = ...) -> None: ...

class Placement(dict):
    def __init__(self, constraints: Optional[Any] = ..., preferences: Optional[Any] = ..., platforms: Optional[Any] = ...) -> None: ...

class PlacementPreference(dict):
    def __init__(self, strategy: Any, descriptor: Any) -> None: ...

class DNSConfig(dict):
    def __init__(self, nameservers: Optional[Any] = ..., search: Optional[Any] = ..., options: Optional[Any] = ...) -> None: ...

class Privileges(dict):
    def __init__(self, credentialspec_file: Optional[Any] = ..., credentialspec_registry: Optional[Any] = ..., selinux_disable: Optional[Any] = ..., selinux_user: Optional[Any] = ..., selinux_role: Optional[Any] = ..., selinux_type: Optional[Any] = ..., selinux_level: Optional[Any] = ...) -> None: ...
