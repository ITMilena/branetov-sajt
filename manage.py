#!/usr/bin/env python
import os
import sys
from pathlib import Path


def _load_dotenv_if_exists():
    """
    Učita promenljive iz .env fajla ako postoji (bez instaliranja python-dotenv).
    Format: KEY=VALUE
    Linije koje počinju sa # se ignorišu.
    """
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        return

    try:
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)
    except Exception:
        # Ako je .env lošeg formata, ne rušimo aplikaciju
        pass


def main():
    _load_dotenv_if_exists()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "branetov_sajt.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django nije pronađen. Proveri da li je instaliran i da li koristiš isti Python."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
