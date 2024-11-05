import logging
from pipeline import build_pipeline
from rules import (
    check_circuit_breaker,
    error_handler,
    check_data_completeness,
    validate_account_numbers,
    check_quarantine_threshold,
    transform_data_format,
    aggregate_data,
    file_processor,
)

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


# Main function to test the middleware pipeline
def main():
    # Sample files for testing
    files = {
        "file1.txt": {
            "file_name": "file1.txt",
            "content": "Account data for processing",
            "account_number": "AB123456",
            "quarantined_accounts": 500_000,
        },
        "file2.txt": {
            "file_name": "file2.txt",
            "content": "Suspicious data",
            "account_number": "XX999999",
            "quarantined_accounts": 1_500_000,
        },  # Fails quarantine threshold
        "file3.txt": {
            "file_name": "file3.txt",
            "content": "Data needing transformation    ",
            "account_number": "CD765432",
            "quarantined_accounts": 200_000,
        },
    }

    # Build the middleware pipeline
    middlewares = [
        check_circuit_breaker,  # Check if circuit breaker is open before processing
        error_handler,
        check_data_completeness,
        validate_account_numbers,
        check_quarantine_threshold,
        transform_data_format,
        aggregate_data,
        file_processor,
    ]
    pipeline = build_pipeline(middlewares)

    # Process each file through the pipeline
    for file_data in files.values():
        try:
            pipeline(file_data)
        except ValueError:
            continue  # Skip to the next file if an error occurred


if __name__ == "__main__":
    main()
