from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Entity:
    id: UUID = field(default_factory=uuid4, init=False)
    name: str
    description: str
