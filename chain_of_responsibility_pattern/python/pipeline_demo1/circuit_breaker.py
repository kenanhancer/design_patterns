import time
import logging
from notification import send_alert


class CircuitBreaker:
    def __init__(self, failure_threshold: int, reset_timeout: int):
        self.failure_threshold = (
            failure_threshold  # Number of failures before opening the circuit
        )
        self.reset_timeout = (
            reset_timeout  # Time in seconds before moving to Half-Open state
        )
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "Closed"

    def is_open(self) -> bool:
        # Check if the circuit is in the Open state
        if self.state == "Open":
            # If enough time has passed, move to Half-Open state
            if time.time() - self.last_failure_time >= self.reset_timeout:
                self.state = "Half-Open"
                logging.info("Circuit breaker moved to Half-Open state.")
            return True
        return False

    def record_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        logging.warning(
            f"Failure recorded. Current failure count: {self.failure_count}"
        )

        # If failures exceed threshold, open the circuit
        if self.failure_count >= self.failure_threshold:
            self.state = "Open"
            logging.error("Circuit breaker opened due to consecutive failures.")
            send_alert("Circuit breaker opened due to consecutive failures.")

    def record_success(self):
        # Reset the circuit if a success occurs in Half-Open state
        if self.state == "Half-Open":
            self.state = "Closed"
            self.failure_count = 0
            logging.info("Circuit breaker closed after successful run.")
