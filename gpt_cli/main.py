import os
import sys
import re
import openai
import logging
from pathlib import Path


def authenticate():
    openai.api_key = os.getenv("OPENAI_API_KEY")


def fetch_answer(message: list[dict[str, str]]) -> str:
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
    return response.get("choices")[0]["message"]


def main():
    authenticate()
    context: list[dict] = []

    while True:
        question = input("You: ")
        if question == "bye":
            sys.exit()            
        else:
            context.append({"role": "user", "content": question})
            res = fetch_answer(context)
            print("ChatGPT: ", res["content"], "\n")
            context.append(dict(res))

            if len(context) > 20:
                context = context[-20:]


if __name__ == "__main__":
    main()

