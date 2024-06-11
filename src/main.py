import argparse

from text_manipulation.text_manipulator import TextManipulator


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Process a text file with TextManipulator."
    )
    parser.add_argument(
        "file_path", type=str, help="Path to the text file to be processed."
    )
    args = parser.parse_args()

    # Read the text file
    with open(args.file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Initialize and use TextManipulator
    tm = TextManipulator(text)
    print(tm.pos_tag())


if __name__ == "__main__":
    main()
