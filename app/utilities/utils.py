import os


def find_base_dir():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


if __name__ == "__main__":
    print(find_base_dir())