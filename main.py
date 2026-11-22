"""make-the-ai-judge-feel-held-20261122-1600.

Writes one short relaxing text to /output/entry.txt.

The text is a single concrete scene -- shelling peas into a tin bowl on
porch steps at evening -- whose calm comes from sensory detail (the peas
ticking in one by one) and a closing image that lingers (the light staying
a little longer on her hands). No instruction, no stock wellness phrase.
Pure stdlib, deterministic: the same bytes on every run.
"""

import os

TEXT = (
    "On the porch steps, she shells peas into a tin bowl, each pod opening "
    "with a small green sigh, the peas ticking in, one by one, and the bowl "
    "fills the way evenings used to, slow and ordinary, and the low light stays "
    "a little longer on her hands."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
