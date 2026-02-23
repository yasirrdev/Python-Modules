from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if not isinstance(data, list):
            raise ValueError("Data must be a list of numbers.")

        for item in data:
            if not isinstance(item, (int, float)):
                raise ValueError("All items must be numeric.")

        print("Validation: Numeric data verified.")
        return True

    def process(self, data) -> str:
        print("Initializing Numeric Processor...")
        print("Processing data: ", data)
        try:
            self.validate(data)

            total = sum(data)
            count = len(data)
            avg = total / count if count > 0 else 0
            result = (
                f"Processed {count} numeric values,"
                f" sum={total}, avg={avg}"
            )
            return self.format_output(result)
        except Exception as e:
            return f"Processing failed: {e}"


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if not isinstance(data, str):
            raise ValueError("Data must be a string.")
        print("Validation: Text data verified.")
        return True

    def process(self, data) -> str:
        print("Initializing Text Processor...")
        print("Processing data: ", data)

        try:
            self.validate(data)
            character_count = len(data)
            word_count = len(data.split())
            result = (
                f"Processed text: {character_count} characters,"
                f" {word_count} words"
            )
            return self.format_output(result)
        except Exception as e:
            return f"Processing failed: {e}"


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        if not isinstance(data, str):
            raise ValueError("Log entry must be a string.")
        if ":" not in data:
            raise ValueError("Invalid log format. Use 'LEVEL: message'.")

        level, _ = data.split(":", 1)
        level = level.strip()

        if level not in ["INFO", "WARNING", "ERROR"]:
            raise ValueError("Invalid log level.")

        print("Validation: Log entry verified.")
        return True

    def process(self, data: Any) -> str:
        print("Initializing Log Processor...")
        print("Processing data: ", data)
        try:
            self.validate(data)

            level, message = data.split(":", 1)
            level = level.strip()
            message = message.strip()

            if level == "ERROR":
                result = f"[ALERT] {level} level detected: {message}"
            else:
                result = f"[{level}] {level} level detected: {message}"
            return self.format_output(result)

        except Exception as e:
            return f"Processing failed: {e}"


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print(numeric.process([1, 2, 3, 4, 5]))
    print()

    print(text.process("Hello Nexus World"))
    print()

    print(log.process("ERROR: Connection timeout"))
    print()

    print("=== Polymorphic Processing Demo ===")

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data_samples = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready"
    ]

    for i in range(len(processors)):
        result = processors[i].process(data_samples[i])
        print(f"Result {i + 1}: {result}")

    print("Foundation systems online. Nexus ready for advanced streams.")
