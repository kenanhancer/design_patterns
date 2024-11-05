from typing import Callable, Any


# Example circuit breaker rule for POC
def check_quarantine_threshold(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    if data.get("quarantined_accounts", 0) > 1_000_000:
        raise ValueError("Quarantined account threshold exceeded")
    return next_fn()
