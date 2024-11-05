from typing import Callable, Any


# Middleware for aggregating data (dummy aggregation example)
def aggregate_data(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    data["aggregated_value"] = len(
        data["content"].split()
    )  # Count words as example aggregation
    return next_fn()
