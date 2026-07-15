from app import mcp


@mcp.prompt()
def create_secure_password_prompt(account: str) -> str:
    """
    Creates a prompt for generating a secure password.
    """

    return f"""
Generate a secure password suitable for a {account} account.

Requirements:
- At least 16 characters
- Include uppercase letters
- Include lowercase letters
- Include numbers
- Include special characters

Also explain why the password is considered strong.
"""