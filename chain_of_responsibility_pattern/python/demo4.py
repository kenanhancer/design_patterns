from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# Type variables for input and output
TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


class Operation(ABC, Generic[TInput, TOutput]):
    @abstractmethod
    def execute(self, data: TInput) -> TOutput:
        pass


class Pipeline(Operation[TInput, TOutput]):
    def __init__(self):
        self.operations: list[Operation[TInput, TOutput]] = []

    def add(self, operation: Operation[TInput, TOutput]) -> "Pipeline[TInput, TOutput]":
        self.operations.append(operation)
        return self

    def execute(self, data: TInput) -> TOutput:
        result = data
        for operation in self.operations:
            result = operation.execute(result)
        return result


# Specific rule classes
class CheckFileSizeOperation(Operation[str, str]):
    def execute(self, data: str) -> str:
        if len(data) > 1024:
            raise ValueError("File size exceeds limit.")
        return data


class CheckSensitiveInfoOperation(Operation[str, str]):
    def execute(self, data: str) -> str:
        if "CONFIDENTIAL" in data:
            raise ValueError("File contains sensitive information.")
        return data


class CheckNotNullOperation(Operation[str, str]):
    def execute(self, data: str) -> str:
        if data is None:
            raise ValueError("Data is None")
        return data


# New Operation to process multiple files
class FileProcessorOperation(Operation[dict[str, str], None]):
    def __init__(self, pipeline: Pipeline[str, str]):
        self.pipeline = pipeline

    def execute(self, files: dict[str, str]) -> None:
        """Process each file through the pipeline."""
        for file_name, file_data in files.items():
            print(f"Processing {file_name}...")
            try:
                self.pipeline.execute(file_data)
                print(f"{file_name} passed all checks.")
            except ValueError as e:
                print(f"{file_name} failed: {e}")


# Main function
def main():
    # Set up the pipeline with validation rules
    pipeline = Pipeline[str, str]()
    pipeline.add(CheckNotNullOperation())
    pipeline.add(CheckFileSizeOperation())
    pipeline.add(CheckSensitiveInfoOperation())

    # Create the file processor operation
    file_processor = FileProcessorOperation(pipeline)

    # Sample files for testing
    files = {
        "file1.txt": "This is some normal data.",
        "file2.txt": "This file contains CONFIDENTIAL information.",
        "file3.txt": "This is a large file" * 100,  # Simulating a large file
    }

    # Process files using FileProcessorOperation
    file_processor.execute(files)


if __name__ == "__main__":
    main()
