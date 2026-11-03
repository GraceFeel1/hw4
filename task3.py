
import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def show_directory(path, indent=""):
    path = Path(path)

    if not path.exists():
        print("Directory does not exist.")
        return

    if not path.is_dir():
        print("The path is not a directory.")
        return

    print(Fore.BLUE + f"📦 {path.name}")

    def print_tree(directory, prefix=""):
        items = sorted(directory.iterdir(), key=lambda item: (item.is_file(), item.name.lower()))

        for index, item in enumerate(items):
            is_last = index == len(items) - 1

            connector = "┗ " if is_last else "┣ "
            new_prefix = prefix + ("   " if is_last else "┃  ")

            if item.is_dir():
                print(Fore.BLUE + prefix + connector + f"📂 {item.name}")
                print_tree(item, new_prefix)
            else:
                print(Fore.GREEN + prefix + connector + f"📜 {item.name}")

    try:
        print_tree(path)

    except PermissionError:
        print(Fore.RED + "Permission denied.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python task3.py <directory_path>")
        return

    path = sys.argv[1]

    show_directory(path)


if __name__ == "__main__":
    main()
