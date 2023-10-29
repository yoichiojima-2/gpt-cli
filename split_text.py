import os
from pathlib import Path
from argparse import ArgumentParser
from tqdm import tqdm


def main(directory: str):
    textfiles = list(Path(directory).glob("*.txt"))
    for i in tqdm(textfiles, total=len(textfiles), desc="splitting text..."):
        split_text_file(i)


def split_text_file(filepath, chunk_size=2000):
    file = Path(filepath)
    with file.open("r", encoding="utf-8") as f:
        content = f.read()
        parts = [
            content[i : i + chunk_size] for i in range(0, len(content), chunk_size)
        ]

    split_path = Path(file.parent / f"split/{file.stem}_split")
    split_path.mkdir(parents=True, exist_ok=True)

    for idx, part in enumerate(parts):
        output_file = split_path / f"{file.stem}_part{idx+1}.txt"
        output_file.write_text(part)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--directory", "-d", type=str)
    args = parser.parse_args()
    main(args.directory)
