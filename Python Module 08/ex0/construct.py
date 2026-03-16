import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    venv_path = os.environ.get('VIRTUAL_ENV', '')
    return os.path.basename(venv_path)


def get_package_path() -> str:
    try:
        return site.getsitepackages()[0]
    except AttributeError:
        return "Unknown"


def main() -> None:
    if is_virtual_env():
        venv_path = os.environ.get('VIRTUAL_ENV', sys.prefix)
        venv_name = get_venv_name()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(get_package_path())
    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
