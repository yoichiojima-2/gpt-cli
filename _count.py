from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint


def main(directory: str):
    p = Path(directory)
    count = {}
    for i in p.glob("*.txt"):
        count[str(i)] = len(i.read_text())
    pprint(count)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--directory", "-d", type=str)
    args = parser.parse_args()
    main(args.directory)
