"""
Demonstration client using the clean-style `ExceptionDemoService`.

The client checks optional return values rather than forcing callers to handle
exceptions for expected, non-exceptional conditions.
"""
from typing import Optional

from .exception_service import ExceptionService, InsufficientBalanceException

try:
    # Import User only for runtime usage in examples; this keeps type imports local.
    from budwing.clean.function.small_function import User
except Exception:
    User = None  # type: ignore


def main() -> None:
    service = ExceptionService()

    user_option: Optional[User] = service.find_user_by_id(1)
    if user_option is not None:
        print(f"User found: {user_option}")
    else:
        print("User not found: 1")

    config_option = service.get_config("request.timeout")
    if config_option is not None:
        print(f"Config: {config_option}")
    else:
        print("Configuration missing for key: request.timeout")

    try:
        service.pay("ACC123", 500.0)
    except InsufficientBalanceException as e:
        print(e)


if __name__ == "__main__":
    main()
