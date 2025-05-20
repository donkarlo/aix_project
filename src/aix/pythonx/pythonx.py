import sys


class Pythonx:
    def __init__(self):
        pass

    @staticmethod
    def print_sys_paths():
        for p in sys.path:
            print(p)