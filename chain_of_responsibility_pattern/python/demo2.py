from typing import Generic, TypeVar

# Define a generic type variable
T = TypeVar("T")


class PipelineStage(Generic[T]):
    def process(self, data: T) -> T:
        raise NotImplementedError("process() must be defined in subclass")


class Pipeline(Generic[T]):
    def __init__(self):
        self.stages: list[PipelineStage[T]] = []

    def add_stage(self, stage: PipelineStage[T]) -> "Pipeline[T]":
        self.stages.append(stage)
        return self  # Return self for chaining

    def execute(self, data: T) -> T:
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class MultiplyStage(PipelineStage):
    def __init__(self, factor: int):
        self.factor = factor

    def process(self, data):
        data = data * self.factor
        print(f"MultiplyStage: Multiplied data by {self.factor}, result: {data}")
        return data


class AddStage(PipelineStage):
    def __init__(self, increment: int):
        self.increment = increment

    def process(self, data):
        data = data + self.increment
        print(f"AddStage: Added {self.increment}, result: {data}")
        return data


class SubtractStage(PipelineStage):
    def __init__(self, decrement: int):
        self.decrement = decrement

    def process(self, data):
        data = data - self.decrement
        print(f"SubtractStage: Subtracted {self.decrement}, result: {data}")
        return data


class DivideStage(PipelineStage):
    def __init__(self, divisor: int):
        self.divisor = divisor

    def process(self, data):
        if self.divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        data = data / self.divisor
        print(f"DivideStage: Divided by {self.divisor}, result: {data}")
        return data


class PowerStage(PipelineStage):
    def __init__(self, power: int):
        self.power = power

    def process(self, data):
        data = data**self.power
        print(f"PowerStage: Raised to the power of {self.power}, result: {data}")
        return data


def main():
    # Create a pipeline with multiple stages
    pipeline = Pipeline()

    pipeline.add_stage(MultiplyStage(2))
    pipeline.add_stage(AddStage(5))
    pipeline.add_stage(SubtractStage(3))
    pipeline.add_stage(DivideStage(2))
    pipeline.add_stage(PowerStage(3))

    # Execute the Pipeline
    initial_data = 10
    result = pipeline.execute(initial_data)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
