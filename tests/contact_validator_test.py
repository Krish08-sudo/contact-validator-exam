import pytest

from src.contact_validator import (
    is_valid_email,
    is_valid_phone,
    mask_email,
    normalize_phone
)


def test_is_valid_email_true():
    email = "student@lpu.in"

    result = is_valid_email(email)

    assert result == True


def test_is_valid_email_type_error():
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    phone = "555-123-4567"

    result = is_valid_phone(phone)

    assert result == True


def test_mask_email_basic():
    """Test masking a typical email address."""
    email = "priya@example.com"

    result = mask_email(email)

    assert result == "pr***@example.com"
