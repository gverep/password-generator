import random
import string

import pytest
from password_generator.utils import generate_password


def test_generate_password_determenistic():
    secret_key = str(random.getrandbits(256))
    subject = str(random.getrandbits(256))
    length = random.randint(8, 100)

    password1 = generate_password(secret_key=secret_key, subject=subject, length=length)
    password2 = generate_password(secret_key=secret_key, subject=subject, length=length)

    assert password1 == password2, f"Passwords are not deterministic: {password1} != {password2}"


def test_generate_password_random():
    secret_key = None
    subject = None
    length = random.randint(8, 100)

    password1 = generate_password(secret_key=secret_key, subject=subject, length=length)
    password2 = generate_password(secret_key=secret_key, subject=subject, length=length)

    assert password1 != password2, f"Passwords are same: {password1} == {password2}"


def test_generate_password_length():
    secret_key = None
    subject = None
    length = random.randint(8, 100)

    password = generate_password(secret_key=secret_key, subject=subject, length=length)
    assert len(password) == length, f"Password length is not {length}: {len(password)}"


def test_generate_password_character_pool():
    secret_key = None
    subject = None
    length = random.randint(8, 100)

    password = generate_password(
        secret_key=secret_key,
        subject=subject,
        length=length,
        use_uppercase=True,
        use_digits=True,
        use_special_chars=True,
    )

    assert any(c.isupper() for c in password), "Password should contain at least one uppercase letter"
    assert any(c.isdigit() for c in password), "Password should contain at least one digit"
    assert any(c in string.punctuation for c in password), "Password should contain at least one special character"


def test_generate_password_missing_secret_key_or_subject():
    secret_key = None
    subject = str(random.getrandbits(256))
    length = random.randint(8, 100)

    with pytest.raises(ValueError):
        generate_password(secret_key=secret_key, subject=subject, length=length)
