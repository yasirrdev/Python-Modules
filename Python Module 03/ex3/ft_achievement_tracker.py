def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print(f"\nAlice's Achievements: {alice}")
    print(f"Bob's Achievements: {bob}")
    print(f"Charlie's Achievements: {charlie}")

    print("=== Achievement Analytics ===")
    all_achievements = alice.union(bob).union(charlie)
    print(f"All Achievements Unlocked: {all_achievements}")
    print(f"Total Unique Achievements: {len(all_achievements)}")

    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Achievements Unlocked by All Players: {common_all}")

    rare = all_achievements.difference(
        alice.intersection(bob).union(alice.intersection(charlie))
        .union(bob.intersection(charlie))
    )
    print(f"Rare Achievements (Unlocked by Only One Player): {rare}")

    alice_bob_common = alice.intersection(bob)
    print(f"Achievements Unlocked by Both Alice and Bob: {alice_bob_common}")

    alice_unique = alice.difference(bob).difference(charlie)
    print(f"Achievements Unique to Alice: {alice_unique}")

    bob_unique = bob.difference(alice).difference(charlie)
    print(f"Achievements Unique to Bob: {bob_unique}")

    charlie_unique = charlie.difference(alice).difference(bob)
    print(f"Achievements Unique to Charlie: {charlie_unique}")


if __name__ == "__main__":
    main()
