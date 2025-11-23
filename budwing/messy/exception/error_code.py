"""
Legacy-style error code example.

This module demonstrates returning integer error codes for legacy systems.
Modern code typically prefers exceptions or result objects with richer context.
"""

def error_code_method() -> int:
    """Return an integer error code when a simulated error condition occurs.

    Returns:
        int: `1001` to indicate a specific error, or `0` for success.
    """
    error_condition = True
    if error_condition:
        return 1001
    return 0
