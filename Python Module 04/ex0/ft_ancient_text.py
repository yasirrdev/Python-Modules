def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")

    try:
        file = open("ancient_fragment.txt", "r")
        # r sirve para abrir el archivo en modo lectura
        print("Connection established...")
        data = file.read()
        print("RECOVERED DATA:")
        print(data)
        file.close()
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
