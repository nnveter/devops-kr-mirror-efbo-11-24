# tests/test_validator.py
from validator import validate_email, validate_phone


def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False


def test_validate_phone():
    for phone in ("+79991234567", "79991234567", "+7 999-123-45-67"):
        assert validate_phone(phone)
    for phone in ("89991234567", "+7999123", "", "+79991234567\n", "+7٩٩٩١٢٣٤٥٦٧"):
        assert not validate_phone(phone)
