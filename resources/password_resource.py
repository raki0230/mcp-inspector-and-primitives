from app import mcp


@mcp.resource("password://policy")
def password_policy() -> str:
    """
    Returns the password generation policy.
    """

    return """
Password Policy

• Default length: 12 characters
• Supports uppercase and lowercase letters
• Supports numbers
• Optional special characters
• Recommended minimum length: 12
• Use 16+ characters for sensitive accounts
"""