"""Simple username validation logic.

Rules enforced by :func:`validate_username`:

1. Must not be empty or only whitespace.
2. Length must be between 3 and 20 characters (inclusive).
3. May only contain letters, digits, and underscores.
4. Must start with a letter.
5. Must not end with an underscore.
6. Must not contain two or more consecutive underscores.
"""

from __future__ import annotations

import re

MIN_LENGTH = 3
MAX_LENGTH = 20

# Allowed character set: letters, digits, underscore.
_ALLOWED_PATTERN = re.compile(r"^[A-Za-z0-9_]+$")


def validate_username(username: str) -> tuple[bool, str]:
    """Validate a username against the project's rules.

    Args:
        username: The candidate username to validate.

    Returns:
        A ``(is_valid, message)`` tuple. ``is_valid`` is ``True`` when the
        username passes every rule. ``message`` is ``"OK"`` on success or a
        human-readable reason for the failure.
    """
    if not isinstance(username, str):
        return False, "Username must be a string."

    if not username or not username.strip():
        return False, "Username must not be empty."

    if len(username) < MIN_LENGTH:
        return False, f"Username must be at least {MIN_LENGTH} characters long."

    if len(username) > MAX_LENGTH:
        return False, f"Username must be at most {MAX_LENGTH} characters long."

    if not _ALLOWED_PATTERN.match(username):
        return False, "Username may only contain letters, digits, and underscores."

    if not username[0].isalpha():
        return False, "Username must start with a letter."

    if username.endswith("_"):
        return False, "Username must not end with an underscore."

    if "__" in username:
        return False, "Username must not contain consecutive underscores."

    return True, "OK"


def is_valid_username(username: str) -> bool:
    """Convenience wrapper returning only the boolean result."""
    valid, _ = validate_username(username)
    return valid
