"""test_app.py - Tests for app.py.

REQ: Test pure functions that return values.

WHY: Pure functions are easy to verify; ensures code works as expected.
"""

from datafun_01_foundations.app_yourname import get_summary


def test_generate_summary_contains_expected_fields() -> None:
    """Verify that generate_summary() returns a formatted string containing key expected values."""
    result = get_summary()

    # Basic type check
    assert isinstance(result, str)

    # Verify the string is not empty
    assert len(result) > 0

    # Verify the notice:
    # Don't forget to add an f at the start of this string to make it an f-string!
    # no longer appears in the string.

    # TODO: Uncomment the line below when you have completed your summary function.
    # assert "Don't forget to add an f at the start of this string to make it an f-string!" not in result
