import logging
from typing import Callable, Any
from circuit_breaker import CircuitBreaker

# Initialize the circuit breaker with a failure threshold and reset timeout
circuit_breaker = CircuitBreaker(failure_threshold=3, reset_timeout=60)


# Middleware to check if circuit breaker is open
def check_circuit_breaker(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    if circuit_breaker.is_open():
        logging.warning("Circuit breaker is open, skipping processing.")
        return {"statusCode": 503, "body": "Service Unavailable"}
    return next_fn()
