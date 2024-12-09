"""
run the main app
"""
from .branches import Branches


def run() -> None:
    reply = Branches().run()
    print(reply)
