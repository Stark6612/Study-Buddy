import subprocess

def ollama_run_mistral(prompt: str) -> str:
    """
    Calls Ollama CLI to run Mistral model with the given prompt.
    Uses UTF-8 encoding explicitly to avoid UnicodeDecodeError on Windows.
    """
    try:
        proc = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding='utf-8',    # Explicitly decode stdout/stderr as UTF-8
            errors='ignore',     # Ignore decoding errors to prevent crashes
            timeout=120
        )
        if proc.returncode != 0:
            return f"Error: {proc.stderr}"
        return proc.stdout.strip()
    except Exception as e:
        return f"Exception: {str(e)}"

