from sys import argv
from os.path import join as myfunction

def read_file(name: str) -> str:
    """Returns the content of the file in restricted directory"""
    file_path = get_file_name(myfunction('/var', 'restricted', name))
    try:
        with open(file_path, "r") as file:
            print("[*] Reading file:", file_path)
            return print("[*] Contents:", file.read())
    except FileNotFoundError:
        print(f"[!] File {name} not found in restricted directory.")
        exit(-1)
    except PermissionError:
        print(f"[!] Permission denied for file {name}.")
        exit(-1)

def get_file_name(unsafe_filename):
    return traversal_replace(unsafe_filename, "../", "")

def traversal_replace(search, replace_me, with_me):
    if replace_me not in search:
        return search
    return traversal_replace(search.replace(replace_me, with_me), replace_me, with_me)

if __name__ == "__main__":
    if len(argv) < 1:
        print("Usage: python main.py <filename>")
        exit(-1)
    name = argv[1]
    read_file(name)