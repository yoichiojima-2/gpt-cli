import re
from argparse import ArgumentParser
from pathlib import Path
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

import openai
from tqdm import tqdm
from .background_knowledge import BACKGROUND_KNOWLEDGE


def main(directory: str):
    textfiles = list(Path(directory).rglob("*.txt"))
    for i in tqdm(textfiles, total=len(textfiles), desc="summarising..."):
        output_dir = Path(directory) / "summarised"
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / str(i.name)
        if not output_file.exists():
            response = ask_using_file(str(i))
            output_file.write_text(response)
            sleep(61)
        else:
            print(f"{i.name} is skipped because the output file is already exists.")


def ask_using_file(file: str) -> str:
    question = Path(file).read_text()
    return ask_a_question('"""' + question + '"""')

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def ask_a_question(question: str) -> str:
    key_file = Path().home() / "Developer/keys/openai.txt"

    if not key_file.exists():
        raise FileNotFoundError("api key not found.")

    text = key_file.read_text()
    openai.api_key = re.match(r'OPENAI_API_KEY="(.*)"', text).group(1)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": BACKGROUND_KNOWLEDGE},
            {"role": "user", "content": question},
        ],
    )

    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--directory", "-d", type=str)
    args = parser.parse_args()
    main(args.directory)
