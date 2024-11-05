from typing import Callable, Any


# Middleware for checking data completeness
def check_data_completeness(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    required_fields = ["file_name", "content", "account_number", "quarantined_accounts"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
    return next_fn()
