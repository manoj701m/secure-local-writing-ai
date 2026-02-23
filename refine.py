import subprocess
import pyperclip
from pathlib import Path

# Load system prompt
prompt_path = Path("prompts/system_prompt.txt")
system_prompt = prompt_path.read_text()

# Read clipboard
clipboard_text = pyperclip.paste().strip()

if not clipboard_text:
    print("Clipboard is empty.")
    exit()

# Combine prompt
final_prompt = f"{system_prompt}\n\nMessage:\n{clipboard_text}"

# Call Ollama
result = subprocess.run(
    ["ollama", "run", "llama3"],
    input=final_prompt.encode(),
    capture_output=True
)

refined_text = result.stdout.decode().strip()

# Replace clipboard
pyperclip.copy(refined_text)

print("\nRefined message copied to clipboard:\n")
print(refined_text)