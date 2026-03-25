import functools
import operator
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b
    }
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire_enchant': functools.partial(
            base_enchantment, power=50, element='fire'
        ),
        'ice_enchant': functools.partial(
            base_enchantment, power=50, element='ice'
        ),
        'lightning_enchant': functools.partial(
            base_enchantment, power=50, element='lightning'
        )
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def cast(arg):
        return f"Unknown spell type: {arg}"

    @cast.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage dealt"

    @cast.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg} applied"

    @cast.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells cast"

    return cast


def main() -> None:
    spells = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


if __name__ == "__main__":
    main()
