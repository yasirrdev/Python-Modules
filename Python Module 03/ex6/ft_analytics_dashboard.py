def main():
    print("=== Game Analytics Dashboard ===")

    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2050]
    active_players = ["alice", "bob", "charlie"]
    regions = ["north", "east", "north", "central"]

    achievements = {
        "alice": ["first_kill", "level_10", "boss_slayer", "treasure_hunter",
                  "speed_demon"],
        "bob": ["first_kill", "level_10", "collector"],
        "charlie": ["level_10", "boss_slayer", "speed_demon",
                    "treasure_hunter", "perfectionist"],
        "diana": ["first_kill"]
    }

    # === Lists Comprehension ===
    print("=== List Comprehension Examples ===")

    high_scorers = [players[i] for i in range(len(scores)) if scores[i] > 2000]
    print("High scorers (>2000):", high_scorers)

    doubled_scores = [score * 2 for score in scores]
    print("Scores doubled:", doubled_scores)

    active = [player for player in players if player in active_players]
    print("Active players:", active)

    # === Dicts Comprehension ===
    print("=== Dict Comprehension Examples ===")

    player_scores = {players[i]: scores[i] for i in range(len(players))}
    print("Player scores:", player_scores)

    score_categories = {
        "high": len([s for s in scores if s > 2000]),
        "medium": len([s for s in scores if 1500 <= s <= 2000]),
        "low": len([s for s in scores if s < 1500])
    }
    print("Score categories:", score_categories)

    achievement_counts = {
        player: len(achievements[player])
        for player in achievements
    }
    print("Achievement counts:", achievement_counts)

    # === Set Comprehension ===
    print("=== Set Comprehension Examples ===")

    unique_players = {player for player in players}
    print("Unique players:", unique_players)

    unique_achievements = {
        achievement
        for player_achivemeents in achievements.values()
        for achievement in player_achivemeents
    }
    print("Unique achievements:", unique_achievements)

    active_regions = {region for region in regions}
    print("Active regions:", active_regions)

    # === Combined Analysis ===
    print("=== Combined Analysis ===")

    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(scores) / len(scores)
    top_player = max(player_scores, key=player_scores.get)

    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achievements)
    print("Average score:", average_score)
    print(
        f"Top performer: {top_player} "
        f"({player_scores[top_player]} points, "
        f"{achievement_counts[top_player]} achievements)"
    )


if __name__ == "__main__":
    main()
