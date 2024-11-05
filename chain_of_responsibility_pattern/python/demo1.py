class Pipeline:
    def __init__(self):
        self.stages = []

    def add_stage(self, stage, on_failure=None):
        self.stages.append((stage, on_failure))

    def run(self, data):
        for stage, on_failure in self.stages:
            try:
                data = stage(data)  # Pass data to the next stage
            except Exception as e:
                print(f"Error in stage {stage.__name__}: {e}")
                if on_failure:
                    on_failure(e, data)  # Call the failure handler
                else:
                    return f"Pipeline stopped due to an error in {stage.__name__}"
        return data


# Example stages
def validate(data):
    print("Validating data...")
    if not data.get("is_valid"):
        raise ValueError("Data is invalid")
    return data


def transform(data):
    print("Transforming data...")
    data["transformed"] = True
    return data


def save(data):
    print("Saving data...")
    if not data.get("transformed"):
        raise ValueError("Data is not transformed, cannot save")
    data["saved"] = True
    return data


# Error handler function
def handle_failure(error, data):
    print(f"Handling error: {error}. Data: {data}")


def main():
    # Setting up the pipeline with stages and error handling
    pipeline = Pipeline()
    pipeline.add_stage(validate, on_failure=handle_failure)
    pipeline.add_stage(transform, on_failure=handle_failure)
    pipeline.add_stage(save, on_failure=handle_failure)

    # Running the pipeline
    input_data = {"is_valid": True}
    output_data = pipeline.run(input_data)
    print("Final data:", output_data)


if __name__ == "__main__":
    main()
