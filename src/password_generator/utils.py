import hashlib
import hmac
import random
import string


def generate_password(
    length=8, secret_key=None, subject=None, use_uppercase=True, use_digits=True, use_special_chars=True
) -> str:
    if secret_key and subject:
        hmac_obj = hmac.new(secret_key.encode(), subject.encode(), hashlib.sha256)
        hashed_password = hmac_obj.hexdigest()
        final_password = hashed_password[:length]
        return final_password
    elif secret_key and not subject or subject and not secret_key:
        raise ValueError("Both secret_key and topic must be provided to generate a deterministic password.")
    else:
        char_pool = string.ascii_lowercase

        if use_uppercase:
            char_pool += string.ascii_uppercase
        if use_digits:
            char_pool += string.digits
        if use_special_chars:
            char_pool += string.punctuation

        password = "".join(random.choice(char_pool) for _ in range(length))
        return password
