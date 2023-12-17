import sys
import re
import openai
import logging
from pathlib import Path


def authenticate():
    key_file = Path().home() / "Developer/keys/openai.txt"
    if not key_file.exists():
        raise FileNotFoundError("api key not found.")
    text = key_file.read_text()
    openai.api_key = re.match(r'OPENAI_API_KEY="(.*)"', text).group(1)


def fetch_answer(message: list[dict[str, str]]) -> str:
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
    return response.get("choices")[0]["message"]


def main():
    context = []
    authenticate()

    while True:
        question = input("You: ")
        if question == "bye":
            sys.exit()            
        else:
            context.append({"role": "user", "content": question})
            res = fetch_answer(context)
            print("ChatGPT: ", res["content"], "\n")
            context.append(dict(res))

            if len(context) > 20:  # limit context size
                context = context[-20:]


if __name__ == "__main__":
    main()

