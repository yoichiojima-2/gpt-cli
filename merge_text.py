from pathlib import Path
from argparse import ArgumentParser
from pprint import pprint


def main(directory):
    files = [str(i) for i in Path(directory).rglob("*.txt")]
    contents = [Path(i).read_text() for i in sorted(files)]
    print({"directory": directory, "files": files, "contents": contents})

    merged_text = "\n".join(contents)

    output_dir = Path(args.directory) / "merged"
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    output_file = Path(output_dir / "merged_text.txt")
    output_file.write_text(merged_text)

    pprint(
        {
            "message": "completed",
            "content": merged_text,
            "file_saved": str(output_file),
            "length": len(merged_text),
        }
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--directory", "-d", type=str)
    args = parser.parse_args()
    print(args)
    main(args.directory)
