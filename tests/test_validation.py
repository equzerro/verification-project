from app.validators import validate_password


def test_valid_password():
    assert validate_password("Strong123") is True


def test_short_password():
    assert validate_password("123") is False


def test_password_without_numbers():
    assert validate_password("StrongPass") is False


def test_password_without_uppercase():
    assert validate_password("strong123") is False