from app.auth import verify_user


def test_correct_user():
    assert verify_user("admin", "admin123") is True


def test_wrong_password():
    assert verify_user("admin", "wrong") is False


def test_unknown_user():
    assert verify_user("ghost", "admin123") is False