"""Modules and associated components."""

from typing import List, Optional, Union

from pydantic.dataclasses import dataclass

from blowhole.core.config import ConfigModel
from blowhole.core.image import BuildRecipe, ImageName, RunRecipe


@dataclass
class Component(ConfigModel):
    """An executable part of a module."""

    recipe: Union[BuildRecipe, RunRecipe]
    compatible: Optional[List[ImageName]] = None
    results: Union[None, ImageName] = None
    description: Optional[str] = None

    def should_run(self, source_image: Optional[ImageName]) -> bool:
        """Should this component be executed for a given source image."""
        if self.compatible is None or source_image is None:
            return True
        else:
            for image in self.compatible:
                if image.is_compatible(source_image):
                    return True
            return False


@dataclass
class Module(ConfigModel):
    """An individual pluggable component of an image."""

    name: str
    components: List[Component]
    description: Optional[str] = None
