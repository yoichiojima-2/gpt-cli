import re
from pathlib import Path
from argparse import ArgumentParser

import openai


def ask_a_question(question: str) -> str:
    key_file = Path().home() / "Developer/api_keys/openai.txt"
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

def ask_using_file(file):
    question = Path(file).read_text()
    return ask_a_question('"""' + question + '"""')


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--file", "-f", type = str)
    args = parser.parse_args()

    response = ask_using_file(args.file)

    print(response)
