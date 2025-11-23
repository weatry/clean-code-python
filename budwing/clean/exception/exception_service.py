"""
Clean-style exception demo service.

This module provides a small, testable service API that prefers returning
`Optional` results for expected absence (instead of using exceptions), and
raises an exception only for a genuine error condition (e.g. payment failure).

Type hints use forward references to the local `User` model to avoid runtime
import cycles during tests.
"""
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from budwing.clean.function.small_function import User


class InsufficientBalanceException(Exception):
    """Raised when an account does not have enough funds for a payment."""


class GeneralDatasource:
    """A lightweight in-memory datasource used for examples and tests."""

    def __init__(self) -> None:
        self.data: dict[int, "User"] = {}
        self.config_data: dict[str, str] = {}
        self.account_balances: dict[str, float] = {}

    def select_user(self, id_: int):
        return self.data.get(id_)

    def get_config(self, key: str) -> Optional[str]:
        return self.config_data.get(key)

    def get_account_balance(self, account_id: str) -> float:
        return self.account_balances.get(account_id, 0.0)


class ExceptionService:
    """Service that demonstrates clean error handling.

    - `find_user_by_id` returns `Optional[User]` when user may be absent.
    - `get_config` returns `Optional[str]` when a configuration value may be missing.
    - `pay` raises `InsufficientBalanceException` for business-level failure.
    """

    def __init__(self) -> None:
        self.datasource = GeneralDatasource()

    def find_user_by_id(self, id_: int) -> Optional["User"]:
        """Return a user by id or `None` when not found."""
        return self.datasource.select_user(id_)

    def get_config(self, key: str) -> Optional[str]:
        """Return a configuration value or `None` when missing."""
        return self.datasource.get_config(key)

    def pay(self, account_id: str, amount: float) -> None:
        """Attempt to withdraw `amount` from `account_id`.

        Raises:
            InsufficientBalanceException: when the account balance is too low.
        """
        balance = self.datasource.get_account_balance(account_id)
        if balance < amount:
            raise InsufficientBalanceException(f"Insufficient balance in account: {account_id}")
