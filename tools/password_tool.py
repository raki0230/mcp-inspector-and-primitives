import random
import string

from app import mcp


@mcp.tool()
def generate_password(length: int = 12, symbols: bool = True) -> str:
    """
    Generate a secure random password.
    """

    characters = string.ascii_letters + string.digits

    if symbols:
        characters += "!@#$%^&*"

    return "".join(random.choice(characters) for _ in range(length))