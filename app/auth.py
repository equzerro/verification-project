from hashlib import sha256

FAKE_DB = {
    "admin": sha256("admin123".encode()).hexdigest()
}


def verify_user(username: str, password: str) -> bool:
    if username not in FAKE_DB:
        return False

    hashed = sha256(password.encode()).hexdigest()

    return FAKE_DB[username] == hashed