import subprocess
import sys
import argparse
import platform
from pathlib import Path
import pyperclip


# ==============================
# Configuration
# ==============================

MODEL_NAME = "secure-llama3"  # Your custom model
OLLAMA_PATH = "/usr/local/bin/ollama"  # Absolute path for macOS
# For Windows later, change to:
# OLLAMA_PATH = r"C:\Users\<User>\AppData\Local\Programs\Ollama\ollama.exe"


# ==============================
# Utilities
# ==============================

def load_prompt():
    prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "system_prompt.txt"

    if not prompt_path.exists():
        sys.exit("System prompt file not found.")

    return prompt_path.read_text().strip()


def refine_text(text):
    system_prompt = load_prompt()

    final_prompt = f"""
{system_prompt}

Rewrite the following message:

{text}
"""

    try:
        result = subprocess.run(
            [
                OLLAMA_PATH,
                "run",
                MODEL_NAME,
            ],
            input=final_prompt,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        sys.exit("Ollama not found at configured path.")

    if result.returncode != 0:
        sys.exit(f"Ollama error:\n{result.stderr}")

    refined = result.stdout.strip()

    if not refined:
        sys.exit("Empty response from model.")

    # Remove accidental meta text
    if "Note:" in refined:
        refined = refined.split("Note:")[0].strip()

    # Remove wrapping quotes
    if refined.startswith('"') and refined.endswith('"'):
        refined = refined[1:-1].strip()

    return refined


# ==============================
# Cross-Platform Sound (No Popups)
# ==============================

def play_sound():
    system = platform.system()

    try:
        if system == "Darwin":
            subprocess.run(
                ["afplay", "/System/Library/Sounds/Glass.aiff"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        elif system == "Windows":
            import winsound
            winsound.MessageBeep(winsound.MB_OK)

        else:
            print("\a", end="", flush=True)

    except Exception:
        pass  # Never crash if sound fails


# ==============================
# CLI Entry
# ==============================

def main():
    parser = argparse.ArgumentParser(
        description="Secure Local Writing AI - Executive-grade message refinement"
    )

    parser.add_argument(
        "--text",
        type=str,
        help="Provide text directly instead of using clipboard",
    )

    parser.add_argument(
        "--sound",
        action="store_true",
        help="Play notification sound after refinement",
    )

    args = parser.parse_args()

    input_text = args.text.strip() if args.text else pyperclip.paste().strip()

    if not input_text:
        sys.exit("No input text found. Provide --text or copy text to clipboard.")

    refined = refine_text(input_text)

    # Replace clipboard
    pyperclip.copy(refined)

    # Play sound (silent mode for shortcut)
    if args.sound:
        play_sound()

    # Print only in normal CLI mode
    if not args.sound:
        print("\nRefined message copied to clipboard:\n")
        print(refined)


if __name__ == "__main__":
    main()