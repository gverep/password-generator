import typer
import logging

import pyperclip

from .utils import generate_password

app = typer.Typer()


@app.command()
def generate(
    length: int = typer.Argument(8, help="Length of the password"),
    secret_key: str = typer.Option(None, help="Secret key for deterministic password generation"),
    subject: str = typer.Option(None, help="Subject for deterministic password generation"),
    uppercase: bool = typer.Option(True, help="Include uppercase letters"),
    digits: bool = typer.Option(True, help="Include digits"),
    special_chars: bool = typer.Option(True, help="Include special characters"),
    copy: bool = typer.Option(False, help="Copy the password to the clipboard"),
):
    password = generate_password(
        length=length,
        secret_key=secret_key,
        subject=subject,
        use_uppercase=uppercase,
        use_digits=digits,
        use_special_chars=special_chars,
    )

    if copy:
        pyperclip.copy(password)
        logging.info("Password copied to clipboard")

    logging.info(f"Generated password: {password}")


if __name__ == "__main__":
    app()
