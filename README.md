# Secure Local Writing AI

A privacy-first, fully local AI writing assistant that transforms informal or weak text into executive-grade professional communication.

Designed for secure environments where cloud AI tools are restricted.

---

## 🎯 Purpose

Secure Local Writing AI helps professionals:

- Rewrite raw text into structured, professional communication
- Remove weak language and filler
- Maintain a disciplined corporate tone
- Operate fully offline using a local LLM
- Preserve data privacy (no cloud APIs)

This tool is built for secure enterprise workflows.

---

## 🏗 High-Level Architecture

User → CLI → Local Ollama Model → Refined Output → Clipboard

All processing happens locally.

- No internet calls  
- No external APIs  
- No telemetry  

For detailed system design, see:

- docs/ARCHITECTURE.md

---

## 🔒 Security Principles

- No cloud API usage
- No external data transmission
- No logging of user messages
- No background monitoring
- No clipboard daemon
- Manual trigger only
- Fully local model execution

All processing remains within your machine boundary.

---

## 📦 Requirements

- Python 3.9+
- macOS or Windows
- Ollama installed
- A local model (e.g., llama3)

Install Ollama:

https://ollama.com

---

## 🤖 Model Setup

Pull base model:

```bash
ollama pull llama3
```

Create a custom disciplined model.

Create a file named:

```
Modelfile
```

Add:

```
FROM llama3

PARAMETER temperature 0.2
PARAMETER top_p 0.9

SYSTEM """
You are an elite executive communication editor operating in an Indian corporate environment.

Rules:
- Output ONLY the rewritten message.
- No explanations.
- No notes.
- No commentary.
- No quotes.
- Keep concise (1–3 sentences).
- Professional Indian corporate tone.
- Remove weak language.
"""
```

Create the model:

```bash
ollama create secure-llama3 -f Modelfile
```

Verify:

```bash
ollama list
```

You should see:

```
secure-llama3
```

---

## 🚀 Installation

Clone repository:

```bash
git clone <your-repo-url>
cd secure-local-writing-ai
```

Install in editable mode:

```bash
pip install -e .
```

This installs the CLI tool:

```
secure-write
```

---

## ⚙ Configuration

Because system shortcuts and app triggers may not inherit your shell PATH, the Ollama binary path is configured explicitly inside:

```
secure_write/cli.py
```

Example (macOS):

```python
OLLAMA_PATH = "/usr/local/bin/ollama"
```

Confirm your path with:

```bash
which ollama
```

---

## 🧪 Usage

### Clipboard Mode

1. Copy text  
2. Run:

```bash
secure-write
```

Paste the refined output.

---

### Direct Text Mode

```bash
secure-write --text "there are many issues and we are trying to fix it"
```

---

### Silent Mode (Sound Only)

```bash
secure-write --sound
```

- Replaces clipboard
- Plays subtle system sound
- No popup
- No console output

Designed for shortcut integration (documented separately).

---

## 📁 Project Structure

```
secure-local-writing-ai/
│
├── pyproject.toml
├── prompts/
│   └── system_prompt.txt
├── secure_write/
│   └── cli.py
└── docs/
    ├── SETUP.md
    └── ARCHITECTURE.md
```

---

## 📘 Documentation

- docs/SETUP.md
- docs/ARCHITECTURE.md

---

## 🧠 Design Philosophy

This tool is intentionally:

- Not a browser extension
- Not an always-on service
- Not connected to cloud AI
- Not a background clipboard monitor

It is a controlled, deterministic, secure local AI wrapper.

Built for professionals who need:

- Precision
- Privacy
- Discipline
- Enterprise compatibility

---

## ⚠ Known Limitations

- Model quality depends on the local LLM.
- Requires Ollama installed.
- Requires manual invocation.
- No automatic background refinement.

---

## 🛣 Future Enhancements

Planned improvements:

- Tone modes (`--mode executive`)
- Config file support
- Word limit enforcement
- Docker sandbox execution
- PyPI publishing
- Model behavior benchmarking

---

## 👤 Author

Manoj Kumar
DevOps Engineer | Kubernetes | Terraform | Secure Automation