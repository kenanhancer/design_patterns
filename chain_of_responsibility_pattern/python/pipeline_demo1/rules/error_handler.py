from typing import Callable, Any
import logging
from notification import send_alert


# Error handling and alerting middleware
def error_handler(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    try:
        result = next_fn()
        return result
    except ValueError as e:
        # Log and alert
        logging.error(f"{data['file_name']} failed: {e}")
        # Example alert logic
        send_alert(f"{data['file_name']} failed due to: {e}")
        raise e  # Reraise to stop further processing
