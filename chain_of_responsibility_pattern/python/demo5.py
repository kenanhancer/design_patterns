import logging
from typing import Callable, Any

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Define the type for middleware functions
Middleware = Callable[[dict[str, Any], Callable[[], Any]], Any]


# Function to build a middleware pipeline
def build_pipeline(middlewares: list[Middleware]) -> Callable[[dict[str, Any]], Any]:
    def wrap(data: dict[str, Any]) -> Any:
        def create_next(mw_index: int) -> Callable[[], Any]:
            if mw_index < len(middlewares) - 1:
                # Pass to the next middleware
                return lambda: middlewares[mw_index](data, create_next(mw_index + 1))
            else:
                # Call the final handler without a next function
                return lambda: middlewares[mw_index](data)

        return create_next(0)()

    return wrap


# Define a middleware function that acts as an operation
def check_not_null(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    if data.get("content") is None:
        raise ValueError("Data is None")
    return next_fn()


def check_file_size(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    if len(data.get("content", "")) > 1024:
        raise ValueError("File size exceeds limit.")
    return next_fn()


def check_sensitive_info(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    if "CONFIDENTIAL" in data.get("content", ""):
        raise ValueError("File contains sensitive information.")
    return next_fn()


# Error handling middleware
def error_handling(data: dict[str, Any], next_fn: Callable[[], Any]) -> Any:
    try:
        result = next_fn()
        return result
    except ValueError as e:
        logging.error(f"{data['file_name']} failed: {e}")


# File processor middleware to print the result after all checks
def file_processor(data: dict[str, Any]) -> Any:
    # If all previous middleware passes, this middleware will be reached
    logging.info(f"{data['file_name']} passed all checks.")

    return {"statusCode": 200, "body": "Processing Complete"}


# Main function to test the middleware pipeline
def main():
    # Sample files for testing
    files = {
        "file1.txt": {"file_name": "file1.txt", "content": "This is some normal data."},
        "file2.txt": {
            "file_name": "file2.txt",
            "content": "This file contains CONFIDENTIAL information.",
        },
        "file3.txt": {
            "file_name": "file3.txt",
            "content": "This is a large file" * 100,
        },  # Simulating a large file
    }

    # Build the middleware pipeline
    middlewares = [
        error_handling,
        check_not_null,
        check_file_size,
        check_sensitive_info,
        file_processor,  # Final step, no next_fn needed
    ]
    pipeline = build_pipeline(middlewares)

    # Process each file through the pipeline
    for file_data in files.values():
        pipeline(file_data)


if __name__ == "__main__":
    main()
