"""
Messy-style exception demo service.

This module intentionally demonstrates a style where business conditions are
implemented as exceptions: callers are forced to handle these cases.
"""
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from budwing.messy.function.small_function import User


class UserNotFoundException(Exception):
    """Raised when a requested user does not exist."""


class ConfigMissingException(RuntimeError):
    """Raised when required configuration is absent."""


class InsufficientBalanceException(Exception):
    """Raised when an account balance is insufficient for a payment."""


class GeneralDatasource:
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
    """Service that raises exceptions for absent business conditions."""

    def __init__(self) -> None:
        self.datasource = GeneralDatasource()

    def find_user_by_id(self, id_: int):
        user = self.datasource.select_user(id_)
        if user is None:
            raise UserNotFoundException(f"User not found: {id_}")
        return user

    def get_config(self, key: str) -> str:
        value = self.datasource.get_config(key)
        if value is None:
            raise ConfigMissingException(f"Configuration missing for key: {key}")
        return value

    def pay(self, account_id: str, amount: float) -> None:
        balance = self.datasource.get_account_balance(account_id)
        if balance < amount:
            raise InsufficientBalanceException(f"Insufficient balance in account: {account_id}")
