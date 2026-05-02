import argparse
from .printer import print_mood


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print text in colour matching its mood"
    )

    parser.add_argument("text", nargs="+", help="Text to analyse")
    parser.add_argument(
        "--scores", action="store_true",
        help="Show mood scores"
    )

    args = parser.parse_args()
    text = " ".join(args.text)

    print_mood(text, show_scores=args.scores)
