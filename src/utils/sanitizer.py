"""
Input sanitization utilities to prevent XSS and injection attacks.
"""

import re
import bleach

# Maximum allowed length for any user input
MAX_INPUT_LENGTH = 2000

# Allowed HTML tags (none — we strip everything)
ALLOWED_TAGS: list[str] = []
ALLOWED_ATTRIBUTES: dict[str, list[str]] = {}


def sanitize_text(raw_input: str) -> str:
    """
    Sanitise user-provided text.

    1. Truncate to MAX_INPUT_LENGTH.
    2. Strip all HTML tags via bleach.
    3. Remove control characters.
    4. Collapse excessive whitespace.

    Args:
        raw_input: Untrusted user string.

    Returns:
        Cleaned string safe for display and API calls.
    """
    if not isinstance(raw_input, str):
        return ""

    # Truncate
    text = raw_input[:MAX_INPUT_LENGTH]

    # Strip HTML
    text = bleach.clean(text, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, strip=True)

    # Remove control characters (keep newlines and tabs)
    text = re.sub(r"[^\S \n\t]+", " ", text)

    # Collapse multiple whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
