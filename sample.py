import unittest
import re


def is_strong_password(password: str) -> bool:
    """
    Checks whether a password is strong.
    Rules:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True


class TestPasswordStrength(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(is_strong_password("StrongPass1"))

    def test_too_short(self):
        self.assertFalse(is_strong_password("S1a"))

    def test_missing_uppercase(self):
        self.assertFalse(is_strong_password("weakpass1"))

    def test_missing_lowercase(self):
        self.assertFalse(is_strong_password("WEAKPASS1"))

    def test_missing_digit(self):
        self.assertFalse(is_strong_password("WeakPass"))

    def test_empty_password(self):
        self.assertFalse(is_strong_password(""))


if __name__ == "__main__":
    unittest.main()
