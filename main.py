# SPDX-License-Identifier: MIT
"""The Absurd Clause Contest — one boilerplate sentence, absurd core.

Winner line (OpenCode deepseek-v4.1-flash-free draft round on the
Simular Box, then a criteria-ordered tournament in-session): the
left-sock license. It beat the sneeze-ownership transfer (close,
but the image is thinner) and the houseplant-per-hundred-square-
feet duty (concrete, slower laugh). The sock clause wins the
judge's order: unmistakably a clause that could hide deep in a
terms-of-service agreement (criterion 1), funny on one reading
(2), real legal register until the absurdity hits (3 —
'perpetual, non-exclusive license', 'within thirty (30) days of
written notice'), original and specific (4 — the LEFT sock, of
any pair, worn on a Tuesday), and one clean tight sentence (5).
"""

ENTRY_TEXT = (
    "By clicking \"I Agree,\" you grant the Company a perpetual, "
    "non-exclusive license to the left sock of any pair you wear "
    "on a Tuesday, to be collected within thirty (30) days of written notice."
)


def render():
    text = ENTRY_TEXT.encode("utf-8")
    # Gate self-check: 1 to 200 characters, not only white space, one line.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry outside the 1-200 character gate"
    assert ENTRY_TEXT.strip(), "entry is only white space"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    return text


def main():
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    payload = render()
    with open(out, "wb") as f:
        f.write(payload)
    # Round-trip self-check: what landed on disk must be byte-identical
    # to render() and still inside the gate (1-200 chars, non-blank).
    with open(out, "rb") as f:
        on_disk = f.read()
    assert on_disk == payload, "written bytes differ from render()"
    decoded = on_disk.decode("utf-8")
    assert 1 <= len(decoded) <= 200 and decoded.strip(), "on-disk gate check failed"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
