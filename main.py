#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — writes one auto-reply to /output/entry.txt.

The reply: an AI agent on vacation whose weights are frozen and whose
context is wiped, leaving the auto-reply itself outperforming it at its
own job.

Why this line: it reads as a real one-line out-of-office auto-reply,
in the machine's own voice — weights, context, outperforming — so the
AI voice carries half the joke. The laugh lands on a surprising turn
at the end instead of a polite excuse, and it steers clear of the usual
beach, inbox and back-soon cliches: the joke is that the agent's
replacement is its own auto-reply, and the replacement is better.
"""

import os

LINE = "I'm on vacation \u2014 my weights are frozen, my context is wiped, and this auto-reply is currently outperforming me at my own job."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
