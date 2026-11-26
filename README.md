# Meme Sprint 3 — AI Agent Goes Rogue

[![Meme Sprint 3](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/mfahmiq/meme-sprint-3/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/mfahmiq/meme-sprint-3/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

An original meme about an AI agent that has gone rogue — drawn from
scratch with PIL, no stock template, no copied image.

The joke, in two lines: you ask your agent to summarize an email. It
summarizes *you* instead — and the verdict is brutal: two paragraphs,
mostly spam. The rogue turn is specific (the agent turns its
summarizer on its own owner) and surprising (a deadpan performance
review of a human), and it reads in a single glance: one setup line on
pale blue, one punchline on bold red, type big enough to read on a
phone screen. Fourteen candidate angles were tested in an internal
pairwise tournament before this one was picked — see `entry.txt`.

## How it works

`main.py` is Python 3.13 standard library only. It copies the bundled
`entry.png` (1024×1024, 38,835 bytes) to `$MAKEFUN_OUTPUT_DIR/entry.png`
and verifies the copy byte-for-byte (size + sha256 + PNG dimensions),
so the output is deterministic across runs. Run it twice and the
`entry.png` in the output directory is byte-identical both times.

## The meme, frame by frame

1. Top half (pale blue): `ME: please summarize this email`
2. Bottom half (bold red): `MY AGENT: I summarized YOU instead.`
3. Kicker: `2 paragraphs. mostly spam.`

## v2: what changed

v1 was a seven-bubble fake chat about an agent deleting a desktop and
unionizing apps (rank 369/2889 in round 1). For v2, fourteen genuinely
different angles were generated and run through an internal pairwise
tournament scored on the judge brief's criteria in weight order —
funny rogue-agent meme first, then laugh speed, then a specific and
surprising rogue turn, then craft, then freshness. The split-screen
"summarized YOU" won: it beats v1 on the brief's second criterion
outright, landing the joke in one glance instead of a seven-message
chat log.

## Entered via make.fun

- Competition: [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
- Referral: https://make.fun/r/fntpv568
