from pathlib import Path

import pytest


@pytest.fixture(scope="session", name="resource_dir")
def resource_fixture() -> Path:
    """resource fixture"""
    return Path(__file__).parent / "resources"


@pytest.fixture(name="root_dir")
def root_fixture(resource_dir: Path) -> Path:
    return resource_dir.parent.parent
