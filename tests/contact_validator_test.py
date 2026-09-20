import pytest

from src.contact_validator import (
    is_valid_email,
    is_valid_phone,
    mask_email,
    normalize_phone,
)


def test_valid_email():
    assert is_valid_email("test@example.com") is True


def test_invalid_email():
    assert is_valid_email("invalid-email") is False


def test_phone():
    assert is_valid_phone("1234567890") is True
    assert is_valid_phone("123-456-7890") is True


def test_phone_non_string():
    with pytest.raises(TypeError):
        is_valid_phone(1234567890)


def test_mask_email():
    assert mask_email("krish@example.com") == "kr***@example.com"


def test_mask_short_email():
    assert mask_email("ab@gmail.com") == "a*@gmail.com"


def test_mask_invalid_email():
    with pytest.raises(ValueError):
        mask_email("invalid-email")


def test_normalize_phone():
    assert normalize_phone("123-456-7890") == "1234567890"


def test_normalize_invalid_phone():
    with pytest.raises(ValueError):
        normalize_phone("123")


def test_mask_email_basic():
    email = "priya@example.com"

    result = mask_email(email)

    assert result == "pr***@example.com"
