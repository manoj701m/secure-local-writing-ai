import subprocess
import sys
import argparse
from pathlib import Path
import pyperclip


MODEL_NAME = "llama3"


def load_prompt():
    prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "system_prompt.txt"
    if not prompt_path.exists():
        print("System prompt file not found.")
        sys.exit(1)
    return prompt_path.read_text().strip()


def refine_text(text):
    system_prompt = load_prompt()

    final_prompt = f"""
{system_prompt}

Rewrite the following message:

{text}
"""

    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=final_prompt,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("Error communicating with Ollama.")
        print(result.stderr)
        sys.exit(1)

    refined = result.stdout.strip()

    # Safety guard against meta-text
    if "Note:" in refined:
        refined = refined.split("Note:")[0].strip()

    return refined


def main():
    parser = argparse.ArgumentParser(description="Secure Local Writing AI")
    parser.add_argument(
        "--text",
        type=str,
        help="Provide text directly instead of using clipboard",
    )

    args = parser.parse_args()

    if args.text:
        input_text = args.text.strip()
    else:
        input_text = pyperclip.paste().strip()

    if not input_text:
        print("No input text found.")
        sys.exit(1)

    refined = refine_text(input_text)

    pyperclip.copy(refined)
    print("\nRefined message copied to clipboard:\n")
    print(refined)


if __name__ == "__main__":
    main()