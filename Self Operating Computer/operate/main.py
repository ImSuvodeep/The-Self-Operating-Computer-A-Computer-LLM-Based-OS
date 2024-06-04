"""
Self-Operating Computer
"""

import argparse
from operate.utils.style import ANSI_BRIGHT_MAGENTA 
from operate.operate import main



def main_entry():
    parser = argparse.ArgumentParser(
        description = "Run the AI Operating Computer with a specified model."
    )
    parser.add_argument(
        "-m",
        "--model",
        help = "Specify the model to use",
        required=False,
        default="gemini-pro-vision",
    )


    parser.add_argument(
        "--voice",
        help = "Use voice input mode",
        action = "store_true",
    )

    parser.add_argument(
        "--verbose",
        help = "Run operate in verbose mode",
        action = "store_true",
    )

    parser.add_argument(
        "--prompt",
        help = "Directly input the objective prompt",
        type = str,
        required=False,
    )

    try:
        args = parser.parse_args()
        main(
            args.model,
            terminal_prompt = args.prompt,
            voice_mode = args.voice,
            verbose_mode = args.verbose
        )

    except KeyboardInterrupt:
        print(f"\n{ANSI_BRIGHT_MAGENTA}Exiting...")

if __name__ == "__main__":
    main_entry()     