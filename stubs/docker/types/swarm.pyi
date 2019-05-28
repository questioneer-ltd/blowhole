# Stubs for docker.types.swarm (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..errors import InvalidVersion
from ..utils import version_lt
from typing import Any, Optional

class SwarmSpec(dict):
    def __init__(self, version: Any, task_history_retention_limit: Optional[Any] = ..., snapshot_interval: Optional[Any] = ..., keep_old_snapshots: Optional[Any] = ..., log_entries_for_slow_followers: Optional[Any] = ..., heartbeat_tick: Optional[Any] = ..., election_tick: Optional[Any] = ..., dispatcher_heartbeat_period: Optional[Any] = ..., node_cert_expiry: Optional[Any] = ..., external_cas: Optional[Any] = ..., name: Optional[Any] = ..., labels: Optional[Any] = ..., signing_ca_cert: Optional[Any] = ..., signing_ca_key: Optional[Any] = ..., ca_force_rotate: Optional[Any] = ..., autolock_managers: Optional[Any] = ..., log_driver: Optional[Any] = ...) -> None: ...

class SwarmExternalCA(dict):
    def __init__(self, url: Any, protocol: Optional[Any] = ..., options: Optional[Any] = ..., ca_cert: Optional[Any] = ...) -> None: ...
