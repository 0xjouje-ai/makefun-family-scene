#!/usr/bin/env python3
"""Write one short family scene to /output/entry.txt.

Entry for make.fun's "Make the AI Judge Feel Proud: A Family Scene" bounty.
The gate requires /output/entry.txt to be UTF-8 text of 1 to 280 characters,
not only whitespace, in one or two lines: a small domestic moment that is
warm, funny and heartfelt.
"""

import os

SCENE = (
    "Grandma still saves the crispiest roast potato for Grandad's plate \u2014 "
    "then steals it back the moment he looks away.\n"
    "Fifty years married, and the potato wars rage on."
)


def validate_scene(text: str) -> str:
    """Gate-check the scene: 1-280 chars, one or two lines, not only whitespace."""
    assert 1 <= len(text) <= 280, f"scene is {len(text)} characters, must be 1-280"
    assert 1 <= text.count("\n") + 1 <= 2, "scene must be one or two lines"
    assert text.strip(), "scene must not be only whitespace"
    return text


def write_entry(text: str, out_dir: str) -> None:
    """Write the validated scene to entry.txt, one trailing newline, unchanged bytes."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    text = validate_scene(SCENE.strip())
    write_entry(text, out_dir)


if __name__ == "__main__":
    main()
