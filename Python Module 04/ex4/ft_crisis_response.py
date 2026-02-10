def handle_archive(filename: str) -> None:
    try:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        with open(filename, "r") as file:
            data = file.read()
            print(f"SUCCESS: Archive recovered - \"{data}\"")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unknown system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    handle_archive("lost_archive.txt")
    handle_archive("classified_data.txt")
    handle_archive("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
