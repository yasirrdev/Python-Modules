from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str]) -> List[Any]:
        """Filter the data batch based on given
        criteria and return the filtered list."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return the current processing statistics."""
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count
        }


class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed_count += len(data_batch)

            temps = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and item.startswith("temp:")
            ]

            avg_temp = sum(temps) / len(temps) if temps else 0

            return (
                f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg_temp:.1f}°C"
            )
        except Exception as e:
            return f"Sensor processing failed: {e}"


class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed_count += len(data_batch)
            return f"Transaction data: {len(data_batch)} operations processed."
        except Exception as e:
            return f"Transaction processing failed: {e}"


class EventStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed_count += len(data_batch)
            return f"Event data: {len(data_batch)} events processed."
        except Exception as e:
            return f"Event processing failed: {e}"


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a new data stream to the processor."""
        self.streams.append(stream)

    def process_all(
            self, data_batches: List[List[Any]]) -> List[str]:
        """Process all data batches across
        all streams and return the results."""
        results = []
        for stream, batch in zip(self.streams, data_batches):
            result = stream.process_batch(batch)
            results.append(result)
        return results

    def show_stats(self) -> None:
        """Display the processing statistics for all streams."""
        for stream in self.streams:
            print(stream.get_stats())


if __name__ == "__main__":

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    transaction_data = ["buy:100", "sell:150", "buy:75"]
    event_data = ["login", "error", "logout"]

    processor.process_all([sensor_data, transaction_data, event_data])

    print("=== Stream Statistics ===")
    processor.show_stats()
