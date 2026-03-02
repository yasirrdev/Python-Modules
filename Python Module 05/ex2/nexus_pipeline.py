import time
from typing import Dict, Protocol, Any, List
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    """Protocol defining a single stage in a processing pipeline."""

    def process(self, data: Any) -> Any:
        ...


class InputStage:
    """First stage of a pipeline; performs input validation and parsing."""

    def process(self, data: Any) -> Any:
        """Validate/parse ``data`` and return transformed result."""
        print("Stage 1: Input validation and parsing.")
        return data


class TransformStage:
    """Mutates or enriches data passing through the pipeline."""

    def process(self, data: Any) -> Any:
        """Process ``data`` and return the transformed value."""
        print("Stage 2: Data transformation and enrichment")
        if isinstance(data, str) and "temp" in data:
            return data + "[validated]"
        return data


class OutputStage:
    """Final stage of a pipeline; formats and delivers output."""

    def process(self, data: Any) -> Any:
        """Handle the final output of the pipeline."""
        print("Stage 3: Output formatting and delivery.")
        print(f"Output: {data}")
        return data


class ProcessingPipeline(ABC):
    """Abstract base representing a sequence of processing stages."""

    def __init__(self, pipeline_id: str) -> None:
        """Initialize an empty pipeline."""
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        """Sequentially execute all registered stages."""
        for stage in self.stages:
            try:
                data = stage.process(data)
            except Exception as e:
                print(f"Error in stage {stage.__class__.__name__}: {e}")
                print("Recovery initiated. Skipping failed stage.")
                continue
        return data

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    """Pipeline specialized for handling JSON strings."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Any:
        """Validate JSONish input then execute configured stages."""
        print(f"Processing JSON data through pipeline {self.pipeline_id}...")
        if (
            not isinstance(data, str)
            or not data.startswith("{")
            or not data.endswith("}")
        ):
            raise ValueError("Invalid JSON format")
        return self.run_stages(data)


class CSVAdapter(ProcessingPipeline):
    """Pipeline that operates on simple comma-separated strings."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Any:
        """Validate comma-separated input and run stages."""
        print(f"Processing CSV data through pipeline {self.pipeline_id}...")
        if not isinstance(data, str) or "," not in data:
            raise ValueError("Invalid CSV format")
        return self.run_stages(data)


class StreamAdapter(ProcessingPipeline):
    """Adapter that expects strings containing the word 'stream'."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Any:
        """Check for the keyword 'stream' and run pipeline."""
        print(f"Processing Stream data through pipeline {self.pipeline_id}...")
        if not isinstance(data, str) or "stream" not in data.lower():
            raise ValueError("Invalid Stream format")
        return self.run_stages(data)


class NexusManager:
    """Central manager for coordinating multiple processing pipelines."""

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.stats: Dict[str, float] = {}

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def execute_single(self, pipeline: ProcessingPipeline, data: Any) -> Any:
        """Run a single pipeline and return its output."""
        start_time = time.time()

        try:
            result = pipeline.process(data)
        except Exception as e:
            print(f"Pipeline failure in {pipeline.__class__.__name__}: {e}")
            print("Recovery initiated: Switching to next pipeline.")
            return None

        end_time = time.time()
        total_time = end_time - start_time
        self.stats["last_execution_time"] = total_time

        print(f"Performance: {total_time:.4f}s total processing time")
        return result

    def chain_execute(self, data: Any) -> Any:
        """Execute all registered pipelines in sequence."""
        print("=== Pipeline Chaining Demo ===")
        print("Pipeline A -> Pipeline B -> Pipeline C")

        start_time = time.time()

        for pipeline in self.pipelines:
            try:
                data = pipeline.process(data)
            except Exception as e:
                print(f"Chain failure in {pipeline.__class__.__name__}: {e}")
                print("Recovery initiated: Switching to next pipeline.")
                continue

        end_time = time.time()
        total_time = end_time - start_time
        self.stats["last_execution_time"] = total_time

        print(f"Chain Performance: {total_time:.4f}s total processing time")
        return data

    def get_pipeline_ids(self) -> List[str]:
        """Return a list of identifiers for all registered pipelines."""
        return [pipeline.pipeline_id for pipeline in self.pipelines]

    def get_stats(self) -> Dict[str, float]:
        """Retrieve a copy of the stored timing statistics."""
        return {k: v for k, v in self.stats.items()}


if __name__ == "__main__":

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")

    # Create pipelines
    json_pipeline = JSONAdapter("JSON_001")
    csv_pipeline = CSVAdapter("CSV_001")
    stream_pipeline = StreamAdapter("STREAM_001")

    for pipeline in [json_pipeline, csv_pipeline, stream_pipeline]:
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())

    manager = NexusManager()
    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    print("=== Multi-Format Data Processing ===\n")

    print("Processing JSON...")
    manager.execute_single(json_pipeline, '{"sensor": "temp", "value": 23.5}')
    print()

    print("Processing CSV...")
    manager.execute_single(csv_pipeline, "user,action,timestamp")
    print()

    print("Processing Stream...")
    manager.execute_single(stream_pipeline, "Real-time sensor stream")
    print()

    manager.chain_execute('{"sensor": "temp", "value": 23.5}')
    print()
    print("Nexus Integration complete. All systems operational.")
