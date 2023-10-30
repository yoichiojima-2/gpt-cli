import re
from pathlib import Path
import openai


def ask_a_question(question: str) -> str:
    key_file = Path().home() / "Developer/keys/openai.txt"

    if not key_file.exists():
        raise FileNotFoundError("api key not found.")

    text = key_file.read_text()
    openai.api_key = re.match(r'OPENAI_API_KEY="(.*)"', text).group(1)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
        ],
    )

    return response["choices"][0]["message"]["content"]