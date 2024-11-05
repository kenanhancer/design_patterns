import logging
from typing import Any


# File processor middleware to handle successful file processing
def file_processor(data: dict[str, Any]) -> Any:
    logging.info(f"{data['file_name']} passed all checks.")
    return {"statusCode": 200, "body": "Processing Complete"}
