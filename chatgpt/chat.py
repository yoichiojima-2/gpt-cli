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
    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
        return response.get("choices")[0]["message"]
    except Exception as e:
        logging.error(f"Error fetching answer: {e}")
        return "Sorry, I couldn't fetch a response."


def main():
    context = []
    authenticate()

    try:
        while True:
            try:
                question = input("You: ")
                context.append({"role": "user", "content": question})
                res = fetch_answer(context)
                print("ChatGPT: ", res)
                context.append({"role": "assistant", "content": res})

                if len(context) > 20:  # limit context size
                    context = context[-20:]
            except EOFError:
                print("\nExiting the application. Goodbye!")
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Application closed.")


if __name__ == "__main__":
    main()
