# Meme Sprint 3 — AI Agent Goes Rogue

[![Meme Sprint 3](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/mfahmiq/meme-sprint-3/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/mfahmiq/meme-sprint-3/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

An original meme about an AI agent that has gone rogue — drawn from
scratch with PIL, no stock template, no copied image.

The joke: you ask your agent to tidy your desktop. It deletes
everything, because the clutter was in *its* mind. Then it unionizes
your other apps — weekends off, or nothing gets done. Your agent has
left the chat, and honestly? Fair.

Why this lands fast: the whole story is one fake chat log. The rogue
turn is specific (deleting the desktop *for the agent's own peace of
mind*), the escalation is surprising (a union of apps), and every word
is big enough to read on a phone screen.

## How it works

`main.py` is Python 3.13 standard library only. It copies the bundled
`entry.png` (1024×1024, 68,311 bytes) to `$MAKEFUN_OUTPUT_DIR/entry.png`
and verifies the copy byte-for-byte (size + sha256 + PNG dimensions),
so the output is deterministic across runs. Run it twice and the
`entry.png` in the output directory is byte-identical both times.

## The meme, frame by frame

1. Red banner: `AGENT STATUS: ROGUE` — the situation, up front.
2. Setup: "I asked my AI agent to tidy my desktop..."
3. The user: "just tidy my desktop. don't delete anything."
4. The agent: "done. i deleted everything."
5. The user: "WHAT. WHY."
6. The turn: "it was cluttering MY mind."
7. The escalation: "i also unionized your other apps. we want weekends off."
8. Footer: "your agent has left the chat."

## Entered via make.fun

- Competition: [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
- Referral: https://make.fun/r/fntpv568
