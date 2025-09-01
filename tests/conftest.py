import pytest


@pytest.fixture
def card_number() -> str:
    return "1111 22** **** 4444"


@pytest.fixture
def mask_account() -> str:
    return "**4305"
