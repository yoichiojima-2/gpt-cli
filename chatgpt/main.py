from argparse import ArgumentParser
from .ask_a_question import ask_a_question

def main(question):
    print(ask_a_question(question))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--question", "-q", type = str)
    args = parser.parse_args()
    main(args.question)
