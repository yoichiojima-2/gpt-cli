from pprint import pprint
from pathlib import Path
from argparse import ArgumentParser


def main(directory: str):
    p = Path(directory)

    count = {}
    for i in p.glob("*.txt"):
        with i.open() as f:
            count[str(i)] = len(f.read())

    pprint(count)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--directory", type=str)
    args = parser.parse_args()
    main(args.directory)
