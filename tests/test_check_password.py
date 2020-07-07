from secrets import token_urlsafe

from passwd import check_password


def test_exposed_passwords():
    exposed_passwords = ["12345", "password", "drowssap", "!@#$%^&*()"]
    for pwd in exposed_passwords:
        assert check_password(pwd) > 0


def test_random_passwords():
    for _ in range(3):
        assert check_password(token_urlsafe(32)) == 0
