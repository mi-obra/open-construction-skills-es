#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"{skill_dir.name}: falta SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    if f"name: {skill_dir.name}" not in text:
        errors.append(f"{skill_dir.name}: el frontmatter name no coincide con la carpeta")
    if "description:" not in text:
        errors.append(f"{skill_dir.name}: falta description")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("ERROR: falta directorio skills/")
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {len(skill_dirs)} skills validadas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
