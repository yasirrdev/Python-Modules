from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args):
        return (spell1(*args), spell2(*args))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args):
        return base_spell(*args) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args):
        if condition(*args):
            return spell(*args)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args):
        return [spell(*args) for spell in spells]
    return sequence


def main() -> None:
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage(power: int) -> int:
        return power

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(damage, 3)
    print(f"Original: {damage(10)}, Amplified: {amplified(10)}")


if __name__ == "__main__":
    main()
