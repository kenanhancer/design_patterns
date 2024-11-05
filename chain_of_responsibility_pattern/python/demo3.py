from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from dataclasses import dataclass


TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")
TData = TypeVar("TData")


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


class UpperCaseOperation(Operation[str, str]):
    def execute(self, data: str) -> str:
        return data.upper()


class LowerCaseOperation(Operation[str, str]):
    def execute(self, data: str) -> str:
        return data.lower()


class RemoveWhitespaceOperation(Operation[str, str]):
    def execute(self, data: str) -> str:
        return data.replace(" ", "")


class CheckNotNullOperation(Operation[str, str]):
    def execute(self, data: str) -> str:
        if data is None:
            raise ValueError("Data is None")
        return data


@dataclass
class CheckStringLenghtOperation(Operation[str, str]):
    max_length: int

    def execute(self, data: str) -> str:
        if len(data) > self.max_length:
            raise ValueError("Data is too long")
        return data


def main():
    # Inner pipeline
    inner_pipeline = Pipeline[str, str]()
    inner_pipeline.add(CheckStringLenghtOperation(15))
    inner_pipeline.add(UpperCaseOperation())

    # Outer pipeline
    outer_pipeline = Pipeline[str, str]()
    outer_pipeline.add(CheckNotNullOperation())
    outer_pipeline.add(inner_pipeline)
    outer_pipeline.add(RemoveWhitespaceOperation())

    # Invoke the outer pipeline
    result = outer_pipeline.execute("Hello, World!")

    print(f"Result: {result}")  # Output: "HELLO,WORLD!"


if __name__ == "__main__":
    main()
