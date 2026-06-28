from src.entities.idea import Idea, IdeaStatus, Priority


def test_idea_model_init():

    # preparation
    name: str = "testing"
    description: str = "test the idea object initialization"

    idea = Idea(
        name = name,
        description = description
    )

    assert idea.name == name
    assert idea.description == description
    assert idea.status == IdeaStatus.DRAFT
    assert idea.priority == Priority.LOW
