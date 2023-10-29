import re
from pathlib import Path
from argparse import ArgumentParser
from tqdm import tqdm

import openai


def ask_using_files_in_directory(directory: str):
    textfiles = list(Path(directory).rglob("*.txt"))
    for i in tqdm(textfiles, total=len(textfiles), desc="summarising..."):
        output_dir = Path(directory) / "summarised"
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / str(i.name)
        if not output_file.exists():
            response = ask_using_file(str(i))
            output_file.write_text(response)
        else:
            print(f"{i.name} is skipped because the output file is already exists.")


def ask_using_file(file: str) -> str:
    question = Path(file).read_text()
    return ask_a_question('"""' + question + '"""')


def ask_a_question(question: str) -> str:
    key_file = Path().home() / "Developer/api_keys/openai.txt"

    if not key_file.exists():
        raise FileNotFoundError("api key not found.")

    text = key_file.read_text()
    openai.api_key = re.match(r'OPENAI_API_KEY="(.*)"', text).group(1)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": Path("background_knowledge.txt").read_text()},
            {"role": "user", "content": question},
        ],
    )

    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--directory", "-d", type=str)
    args = parser.parse_args()
    ask_using_files_in_directory(args.directory)
