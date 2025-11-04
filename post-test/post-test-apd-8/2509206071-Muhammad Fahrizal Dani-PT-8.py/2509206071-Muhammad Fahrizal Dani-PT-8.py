from menu import menu_utama

if __name__ == "__main__":
    try:
        menu_utama()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan.")
    except Exception as e:
        print(f"\nError: {e}")