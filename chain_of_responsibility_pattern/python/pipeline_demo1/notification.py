import logging


def send_alert(message: str):
    # Send alert to monitoring channel (e.g., using logging for this example)
    logging.info(f"Alert: {message}")
