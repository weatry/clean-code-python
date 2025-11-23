"""
Client that uses the messy exception service.

Python does not have checked exception. Client are not forced to handle exceptions.
But the final clients may still have to handle them, 
otherwise the exceptions will be thrown to the interpreter,
which may lead to a crash. If that is not what you expected, 
you must handle it and covert it to a user friendly message, 
or let the program exit gracefully.

EAFP(Easier to Ask for Forgiveness than Permission) vs. LBYL(Look Before You Leap)
"""
from .exception_service import (
    ExceptionService,
    UserNotFoundException,
    ConfigMissingException,
    InsufficientBalanceException,
)


def main() -> None:
    service = ExceptionService()

    try:
        service.find_user_by_id(1)
    except UserNotFoundException as e:
        print(e)

    try:
        config = service.get_config("request.timeout")
        print(f"Config: {config}")
    except ConfigMissingException as e:
        print(e)

    try:
        service.pay("ACC123", 500.0)
    except InsufficientBalanceException as e:
        print(e)


if __name__ == "__main__":
    main()
