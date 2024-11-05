from typing import Callable, Any


# Middleware for transforming data format
def transform_data_format(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    data["content"] = data["content"].strip().upper()
    return next_fn()
