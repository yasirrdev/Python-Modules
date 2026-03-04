from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")

    elite = EliteCard("Arcane Warrior", 6, "Legendary", 5, 8, 4)

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    print(f"Attack result: {elite.attack('Enemy')}")
    print(f"Defense result: {elite.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
