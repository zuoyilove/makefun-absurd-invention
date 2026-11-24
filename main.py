# One-Sentence Absurd Invention Pitch — make.fun entry
# (u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
#
# One sentence pitching a ridiculous invention that fixes a tiny
# everyday annoyance, written as plain text to /output/entry.txt.
# The line is a fixed string: the grader runs the program twice and the
# runs must be deterministic, so there is no randomness and no input.
# The gate allows 1 to 220 characters, one sentence.

LINE = (
    "A sock that files a formal complaint each time the wash loses "
    "it, so the dryer finally has to answer for its crimes."
)

MAX_CHARS = 220


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, gate is 1-220"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "entry must not be only whitespace / padded"
    assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be one sentence"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
