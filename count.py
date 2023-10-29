from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint


def main(directory: str):
    p = Path(directory)

    count = {}
    for i in p.glob("*.txt"):
        with i.open() as f:
            count[str(i)] = len(f.read())

    pprint(count)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--directory", "-d", type=str)
    args = parser.parse_args()
    main(args.directory)
