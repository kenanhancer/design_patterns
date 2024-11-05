import re
from typing import Callable, Any


# Middleware for validating account number format
def validate_account_numbers(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    account_number = data.get("account_number", "")
    if not re.match(r"^[A-Z]{2}\d{6}$", account_number):
        raise ValueError("Invalid account number format")
    return next_fn()
