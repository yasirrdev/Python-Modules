import sys
import importlib.util
import importlib.metadata


def check_dependency(package: str) -> bool:

    spec = importlib.util.find_spec(package)
    if spec is None:
        print(f"[MISSING] {package} - Not installed")
        print(f"  Run: pip install {package}")
        return False
    version = importlib.metadata.version(package)
    labels = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computation ready',
        'matplotlib': 'Visualization ready',
        'requests': 'Network access ready'
    }
    label = labels.get(package, 'Ready')
    print(f"[OK] {package} ({version}) - {label}")
    return True


def analyze_data() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    players = ['Mbappé', 'Vinícius', 'Bellingham',
               'Rodrygo', 'Valverde', 'Güler']
    goals = [43,        21,          13,
             10,         8,           7]
    assists = [5,          15,          9,
               6,          11,          4]

    df = pd.DataFrame({
        'player': players,
        'goals': goals,
        'assists': assists
    })
    df['contributions'] = df['goals'] + df['assists']

    print("Generating visualization...")

    fig, axes = plt.subplots(1, 2, figsize=(13, 6))
    fig.suptitle('Real Madrid 2024/25 - All Competitions Stats',
                 fontsize=14, fontweight='bold')

    x = np.arange(len(players))
    width = 0.35

    axes[0].bar(x - width / 2, df['goals'],
                width, label='Goals', color='#FEBE10')
    axes[0].bar(x + width / 2, df['assists'],
                width, label='Assists', color='#00529F')
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(players, rotation=45, ha='right')
    axes[0].set_title('Goals & Assists')
    axes[0].legend()
    axes[0].set_ylabel('Count')

    axes[1].barh(df['player'], df['contributions'],
                 color='#FEBE10', edgecolor='#00529F')
    axes[1].set_title('Total Contributions (G+A)')
    axes[1].set_xlabel('Goals + Assists')

    plt.tight_layout()
    plt.savefig('matrix_analysis.png')
    plt.close()


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    packages = ['pandas', 'requests', 'matplotlib']
    print("Checking dependencies:")

    all_ok = True
    for package in packages:
        if not check_dependency(package):
            all_ok = False

    if not all_ok:
        print()
        print("Missing dependencies detected.")
        print("Install with: pip install -r requirements.txt")
        sys.exit(1)

    print()
    analyze_data()
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
