import re


def is_valid_email(email):
    """Return True if email matches a basic pattern."""
    if not isinstance(email, str):
        raise TypeError("email must be a string")
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    """Return True if phone is exactly 10 digits, optionally with dashes."""
    if not isinstance(phone, str):
        raise TypeError("phone must be a string")
    digits_only = phone.replace("-", "")
    return digits_only.isdigit() and len(digits_only) == 10


def mask_email(email):
    """Mask an email address. Assumes email is already valid."""
    if not is_valid_email(email):
        raise ValueError("email is not valid")

    local, domain = email.split("@")

    if len(local) <= 2:
        masked_local = local[0] + "*" * (len(local) - 1)
    else:
        masked_local = local[:2] + "*" * (len(local) - 2)

    return f"{masked_local}@{domain}"


def normalize_phone(phone):
    """Return phone as digits-only."""
    if not is_valid_phone(phone):
        raise ValueError("phone is not valid")

    return phone.replace("-", "")