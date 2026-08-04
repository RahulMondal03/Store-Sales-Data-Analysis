"""Automated tests for the username validation flow.

Run with either:
    python -m unittest discover -s username_validation/tests
or (if pytest is installed):
    pytest username_validation/tests
"""

import os
import sys
import unittest

# Make the parent package importable when run directly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from validator import is_valid_username, validate_username  # noqa: E402


class TestValidUsernames(unittest.TestCase):
    """Usernames that should pass validation."""

    VALID = [
        "abc",
        "john_doe",
        "User123",
        "a1_b2_c3",
        "Rahul_Mondal",
        "x" + "y" * 19,  # exactly 20 characters
    ]

    def test_valid_usernames_pass(self):
        for name in self.VALID:
            with self.subTest(username=name):
                valid, message = validate_username(name)
                self.assertTrue(valid, f"expected valid, got: {message}")
                self.assertEqual(message, "OK")
                self.assertTrue(is_valid_username(name))


class TestInvalidUsernames(unittest.TestCase):
    """Usernames that should fail validation, with the expected reason fragment."""

    CASES = [
        ("", "empty"),
        ("   ", "empty"),
        ("ab", "at least"),
        ("x" * 21, "at most"),
        ("1abc", "start with a letter"),
        ("_abc", "start with a letter"),
        ("john doe", "letters, digits, and underscores"),
        ("john-doe", "letters, digits, and underscores"),
        ("john.doe", "letters, digits, and underscores"),
        ("café_user", "letters, digits, and underscores"),
        ("john_", "end with an underscore"),
        ("john__doe", "consecutive underscores"),
    ]

    def test_invalid_usernames_fail(self):
        for name, fragment in self.CASES:
            with self.subTest(username=name):
                valid, message = validate_username(name)
                self.assertFalse(valid, f"expected invalid for {name!r}")
                self.assertIn(fragment, message)
                self.assertFalse(is_valid_username(name))


class TestNonStringInput(unittest.TestCase):
    """Non-string inputs should be rejected gracefully."""

    def test_non_string_inputs(self):
        for value in (None, 123, ["abc"], {"a": 1}):
            with self.subTest(value=value):
                valid, message = validate_username(value)
                self.assertFalse(valid)
                self.assertIn("string", message)


if __name__ == "__main__":
    unittest.main(verbosity=2)
