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

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    ) -> List[Any]:

        if criteria == "high_temp":
            return [
                    item for item in data_batch 
                    if item.startswith("temp:") and
                    float(item.split(":")[1]) > 30
                ]

        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:

        try:
            self.processed_count += len(data_batch)
            total_amount = 0

            for item in data_batch:
                action, value = item.split(":")
                value = float(value)
                if action == "buy":
                    total_amount += value
                elif action == "sell":
                    total_amount -= value
            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {total_amount:+.0f} units"
            )

        except Exception as e:
            return f"Transaction processing failed: {e}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    ) -> List[Any]:

        if criteria == "large":
            return [
                    item for item in data_batch 
                    if float(item.split(":")[1]) > 100
                ]

        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:

        try:
            self.processed_count += len(data_batch)
            error_count = sum(
                1 for item in data_batch
                if isinstance(item, str) and item.lower() == "error"
            )
            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{error_count} error detected"
            )
        except Exception as e:
            return f"Event processing failed: {e}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    ) -> List[Any]:

        if criteria == "critical":
            return [
               item for item in data_batch if item.lower() == "error"]

        return super().filter_data(data_batch, criteria)


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

    # === SENSOR STREAM  ===

    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("sensor_001")
    print(f"Stream ID: {sensor_stream.stream_id}, Type: Environmental Data")

    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print("Processing sensor batch: ", sensor_data)
    print(sensor_stream.process_batch(sensor_data))
    print()

    # === TRANSACTION STREAM  ===

    print("Initializing Transaction Stream...")
    transaction_stream = TransactionStream("transaction_001")
    print(f"Stream ID: {transaction_stream.stream_id}, Type: Financial Data")

    transaction_data = ["buy:100", "sell:150", "buy:75"]
    print("Processing transaction batch: ", transaction_data)
    print(transaction_stream.process_batch(transaction_data))
    print()

    # === EVENT STREAM  ===

    print("Initializing Event Stream...")
    event_stream = EventStream("event_001")
    print(f"Stream ID: {event_stream.stream_id}, Type: System Events")

    event_data = ["login", "error", "logout", "error"]
    print("Processing event batch: ", event_data)
    print(event_stream.process_batch(event_data))
    print()

    # === POLYMORPHIC PROCESSING ===

    print("=== Polymorphic Stream Processing ===")
    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    data_batches = [
        ["temp:28.0", "temp:32.5", "temp:25.0"],
        ["buy:200", "sell:50", "buy:150"],
        ["login", "error", "error", "logout"]
    ]

    results = processor.process_all(data_batches)
    for result in results:
        print(result)
    print()

    # === FILTERING ===

    print("Stream filtering active: High-priority data only")
    high_temps = sensor_stream.filter_data(data_batches[0], "high_temp")
    large_transactions = transaction_stream.filter_data(
        data_batches[1], "large")
    critical_events = event_stream.filter_data(data_batches[2], "critical")

    print(f"Filtered results: "
          f"{len(high_temps)} critical sensor alerts, "
          f"{len(large_transactions)} large transactions, "
          f"{len(critical_events)} critical events")
    print()

    print("All streams processed successfully. Nexus throughput optimal.")
