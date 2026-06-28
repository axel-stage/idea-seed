from dataclasses import dataclass
from enum import Enum

from src.entities.entity import Entity


class PainLevel(Enum):
    TRIVIAL = 1
    LOW = 2
    MODERATE = 3
    HIGH = 4
    CRITICAL = 5


@dataclass
class Problem(Entity):
    frequency: int
    drawbacks: list[str]
    pain_level: PainLevel = PainLevel.LOW
