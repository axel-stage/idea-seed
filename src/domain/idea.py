from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timezone

from src.domain.entity import Entity


class IdeaStatus(Enum):
    DRAFT = "DRAFT"
    REJECT = "REJECT"
    APPROVE = "APPROVE"


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class Idea(Entity):
    status: IdeaStatus = IdeaStatus.DRAFT
    priority: Priority = Priority.LOW
    created_at: datetime = datetime.now(timezone.utc)

    def approve_idea(self) -> None:
        if self.status != IdeaStatus.DRAFT:
            raise ValueError("Only ideas with status \"DRAFT\" can be approved.")
        self.status = IdeaStatus.APPROVE

    def reject_idea(self) -> None:
        if self.status != IdeaStatus.DRAFT:
            raise ValueError("Only ideas with status \"DRAFT\" can be rejected.")
        self.status = IdeaStatus.REJECT



