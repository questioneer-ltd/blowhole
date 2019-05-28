# Stubs for docker.api.plugin (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class PluginApiMixin:
    def configure_plugin(self, name: Any, options: Any): ...
    def create_plugin(self, name: Any, plugin_data_dir: Any, gzip: bool = ...): ...
    def disable_plugin(self, name: Any): ...
    def enable_plugin(self, name: Any, timeout: int = ...): ...
    def inspect_plugin(self, name: Any): ...
    def pull_plugin(self, remote: Any, privileges: Any, name: Optional[Any] = ...): ...
    def plugins(self): ...
    def plugin_privileges(self, name: Any): ...
    def push_plugin(self, name: Any): ...
    def remove_plugin(self, name: Any, force: bool = ...): ...
    def upgrade_plugin(self, name: Any, remote: Any, privileges: Any): ...
