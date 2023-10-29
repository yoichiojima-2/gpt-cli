from pathlib import Path
from argparse import ArgumentParser

from split_text import main as split
from merge_text import main as merge
from summarise_split_text import main as summarise


def main(target):
    target = Path(target)
    split(target)
    summarise(target / "split")
    merge(target / "split/summarised")
    split(target / "split/summarised/merged'")
    summarise(target / "split/summarised/merged/split")
    merge(target / "split/summarised/merged/split/summarised")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--target", "-t", type = str)
    args = parser.parse_args()

    main(args.target)