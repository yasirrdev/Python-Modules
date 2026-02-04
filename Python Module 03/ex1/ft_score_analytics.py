import sys


def main():

    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided.")
        return

    scores = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Ignoring invalid score: {arg}")
    if len(scores) == 0:
        print("No valid scores to analyze.")
        return
    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    highest_score = max(scores)
    lowest_score = min(scores)
    score_range = highest_score - lowest_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {highest_score}")
    print(f"Low score: {lowest_score}")
    print(f"Score range: {score_range}")


if __name__ == '__main__':
    main()
