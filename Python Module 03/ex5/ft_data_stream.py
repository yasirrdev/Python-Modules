def game_event_stream(limit: int):
    players = ['Alice', 'Bob', 'Charlie']
    events = ['killed monster', 'found treasure', 'leveled up']

    for i in range(1, limit + 1):
        player = players[i % len(players)]
        level = (i * 3) % 5
        event = events[i % len(events)]
        yield (i, player, level, event)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator():
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    high_level = 0
    treasure_event = 0
    level_up_event = 0
    processed = 0

    stream = game_event_stream(total_events)

    for event_id, player, level, event in stream:
        processed += 1
        if processed <= 3:
            print(f"Event {event_id}: Player {player} (level {level}) {event}")

        if level >= 10:
            high_level += 1
        if event == 'found treasure':
            treasure_event += 1
        if event == 'leveled up':
            level_up_event += 1

    print("=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level-up events: {level_up_event}")
    print("Memory usage: Constant (streaming)")

    print("=== Generator Demonstration ===")
    fib = fibonacci_generator()
    print("Fibonacci sequence (first 10):", end=" ")
    for _ in range(10):
        print(next(fib), end=" ")
    print()
    primes = prime_generator()
    print("Prime numbers (first 5):", end=" ")
    for _ in range(5):
        print(next(primes), end=" ")
    print()


if __name__ == "__main__":
    main()
